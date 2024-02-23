import bpy
from bpy.types import Panel
from .utils import print


class GCT_PT_ArrayImportPanel(Panel):
    bl_label = "GIANTS Array Import"
    bl_idname = "GCT_PT_ArrayImportPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'GIANTS Array Tool'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        gct_props = context.scene.giants_curve_tool
        layout = self.layout

        row = layout.row()
        row.prop(gct_props, "path")
        row = layout.row()
        row.prop(gct_props, "build_curves_while_importing")
        row = layout.row()
        if not gct_props.path:
            row.enabled = False
        row.operator("gct.import_curve", text="Import")
        row = layout.row()
        row.operator("gct.build_curve_selected", text="Build Curve Selected")


class GCT_PT_ArrayExportPanel(Panel):
    bl_label = "GIANTS Array Export"
    bl_idname = "GCT_PT_ArrayExportPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'GIANTS Array Tool'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        gct_props = context.scene.giants_curve_tool
        layout = self.layout

        pass


class GCT_PT_EmptyPanel(Panel):
    bl_label = "GIANTS Array Export"
    bl_idname = "GCT_PT_EmptyPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'data'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type == 'EMPTY'

    def draw(self, context):
        gct_props = context.object.giants_empty_tool
        layout = self.layout

        row = layout.row()
        row.prop(gct_props, "root")
        if gct_props.root:
            row = layout.row()
            row.prop(gct_props, "array_name")
        row = layout.row()
        row.active = gct_props.unlock_export_position
        if gct_props.unlock_export_position:
            row.prop(gct_props, "export_position")
        else:
            row.label(text="Export Position")
        row.prop(gct_props, "unlock_export_position", text="", icon='UNLOCKED' if gct_props.unlock_export_position else 'LOCKED', emboss=False)
        row = layout.row()
        row.active = gct_props.unlock_export_rotation
        if gct_props.unlock_export_rotation:
            row.prop(gct_props, "export_rotation")
        else:
            row.label(text="Export Rotation")
        row.prop(gct_props, "unlock_export_rotation", text="", icon='UNLOCKED' if gct_props.unlock_export_rotation else 'LOCKED', emboss=False)
        row = layout.row()
        row.prop(gct_props, "export_scale")
