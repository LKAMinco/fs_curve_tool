import bpy
from .ui import GCT_PT_ArrayImportPanel, GCT_PT_EmptyPanel, GCT_PT_ArrayExportPanel
from .import_tool import GCT_OT_ImportCurve, GCT_OT_BuildCurveSelected
from .attributes import GCT_Properties, GCT_EmptyProperties

bl_info = {
    "name": "GIANTS Curve Tool",
    "author": "LKAMinco",
    "description": "Tools that can import and export arrays",
    "blender": (2, 80, 0),
    "location": "View3D",
    "warning": "",
    "category": "Generic"
}

classes = (
    GCT_Properties,
    GCT_EmptyProperties,
    GCT_PT_ArrayImportPanel,
    GCT_PT_ArrayExportPanel,
    GCT_PT_EmptyPanel,
    GCT_OT_ImportCurve,
    GCT_OT_BuildCurveSelected
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.giants_curve_tool = bpy.props.PointerProperty(type=GCT_Properties)
    bpy.types.Object.giants_empty_tool = bpy.props.PointerProperty(type=GCT_EmptyProperties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.giants_curve_tool
    del bpy.types.Object.giants_empty_tool
