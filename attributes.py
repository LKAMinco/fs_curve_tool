from bpy.props import StringProperty, EnumProperty, BoolProperty
from bpy.types import PropertyGroup
from .utils import print


class GCT_Properties(PropertyGroup):
    def path_setter(self, value: str):
        self['path'] = value
        return None

    def path_getter(self):
        if 'path' not in self:
            return ''
        return self['path'] if self['path'].endswith('.dds') else ''

    path: StringProperty(
        name="Path",
        description="Path to the file",
        maxlen=1024,
        subtype='FILE_PATH',
        set=path_setter,
        get=path_getter
    )

    build_curves_while_importing: BoolProperty(
        name="Build Curves",
        description="Build curves while importing",
        default=True
    )


class GCT_EmptyProperties(PropertyGroup):
    export_position: BoolProperty(
        name="Export Position",
        description="Export position with the curve",
        default=True
    )

    unlock_export_position: BoolProperty(
        name="Unlock Position",
        description="Not recommended to not export position",
        default=False
    )

    export_rotation: BoolProperty(
        name="Export Rotation",
        description="Export rotation with the curve",
        default=True
    )

    unlock_export_rotation: BoolProperty(
        name="Unlock Rotation",
        description="Not recommended to not export rotation",
        default=False
    )

    export_scale: BoolProperty(
        name="Export Scale",
        description="Export scale with the curve",
        default=False
    )

    root: BoolProperty(
        name="Root",
        description="Is the root of the array",
        default=False
    )

    array_name: StringProperty(
        name="Name",
        description="Name of the array that will be created",
        default="curveArray"
    )
