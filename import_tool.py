import bpy
from bpy.types import Operator
from bpy.props import EnumProperty, IntProperty, BoolProperty
from .curveTool import DDSFile

from .utils import print, to_euler
from bpy.path import abspath


class Counter:
    def __init__(self):
        self._array_counter = 0
        self._pose_counter = 0
        self._parent_counter = 0
        self._curve_counter = 0

    @property
    def array_counter(self):
        self._array_counter += 1
        return self._array_counter

    @array_counter.setter
    def array_counter(self, value):
        self._array_counter = value

    @property
    def pose_counter(self):
        self._pose_counter += 1
        return self._pose_counter

    @pose_counter.setter
    def pose_counter(self, value):
        self._pose_counter = value

    @property
    def parent_counter(self):
        self._parent_counter += 1
        return self._parent_counter

    @parent_counter.setter
    def parent_counter(self, value):
        self._parent_counter = value

    @property
    def curve_counter(self):
        self._curve_counter += 1
        return self._curve_counter

    @curve_counter.setter
    def curve_counter(self, value):
        self._curve_counter = value


class GCT_OT_ImportCurve(Operator):
    bl_idname = "gct.import_curve"
    bl_label = "Import Curve"
    bl_description = "Import a curve from a file"
    bl_options = {'REGISTER', 'UNDO'}

    reset_array_counter: BoolProperty(name='Reset Array Counter', default=True)
    reset_pose_counter: BoolProperty(name='Reset Pose Counter', default=True)
    reset_parent_counter: BoolProperty(name='Reset Parent Counter', default=True)
    reset_curve_counter: BoolProperty(name='Reset Curve Counter', default=True)

    counter = Counter()

    def execute(self, context):
        gtc_props = context.scene.giants_array_tool
        path = abspath(gtc_props.path)
        with open(path, 'rb') as file:
            data = file.read()
        dds_file = DDSFile(data)
        if dds_file.objects is None or dds_file.configuration is None:
            self.report({'ERROR'}, 'Invalid file, file does not have array structure')
            return {'CANCELLED'}

        max_obj_count = dds_file.configuration['max_num_of_objects']
        hide_first_and_last = dds_file.configuration['hide_first_and_last']

        if self.reset_array_counter:
            self.counter.array_counter = 0
        if self.reset_pose_counter:
            self.counter.pose_counter = 0
        if self.reset_parent_counter:
            self.counter.parent_counter = 0
        if self.reset_curve_counter:
            self.counter.curve_counter = 0

        name = 'curveArray' + str(self.counter.array_counter)
        empty_root = self.setup_empty(name)
        empty_root.giants_array_tool.root = True
        empty_root.giants_array_tool.array_name = name

        for key, value in dds_file.objects.items():
            empty_pose = self.setup_empty('pose' + str(self.counter.pose_counter), empty_root)
            empty_parent = None
            for idx, (pos, rot, scale) in enumerate(zip(value['location'], value['rotation'], value['scale'])):
                # print(f'pos {pos}, rot {rot}, scale {scale}')
                if idx % max_obj_count == 0:
                    empty_parent = self.setup_empty('parent' + str(self.counter.parent_counter), empty_pose)
                if hide_first_and_last:
                    if pos[3] == 0.0 and idx % max_obj_count != 0 and idx % max_obj_count != max_obj_count - 1:
                        continue
                else:
                    if pos[3] == 0.0:
                        continue

                empty_curve = self.setup_empty('curve' + str(self.counter.curve_counter), empty_parent)
                empty_curve.location = pos[0], -1 * pos[2], pos[1]
                empty_curve.rotation_euler = to_euler(rot)
                empty_curve.scale = scale[:3]

        return {'FINISHED'}

    @staticmethod
    def setup_empty(name, parent=None):
        empty = bpy.data.objects.new(name, None)
        bpy.context.collection.objects.link(empty)
        empty.parent = parent
        empty.empty_display_type = 'ARROWS'
        empty.empty_display_size = 0.25
        return empty


class GCT_OT_BuildCurveSelected(Operator):
    bl_idname = "gct.build_curve_selected"
    bl_label = "Build Curve"
    bl_description = "Import a curve from a file"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type == 'EMPTY'

    def execute(self, context):
        return {'FINISHED'}
