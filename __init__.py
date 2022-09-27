bl_info = {
    "name": "CreateCameraPass",
    "author": "Chii",
    "version": (3, 0),
    "blender": (3, 3, 0),
    "location": "3D viewport > add > Create Passed Camera",
    "description": "Create Camera Pass",
    "warning": "",
    "support": "TESTING",
    "doc_url": "",
    "tracker_url": "",
    "category": "Object"
}

if "bpy" in locals():
    import imp
    imp.reload(create_camera_pass)
else:
    from . import create_camera_pass
    
import bpy
from bpy.types import PropertyGroup

from bpy.props import (
    CollectionProperty,
    IntProperty,
    BoolProperty,
    StringProperty,
    PointerProperty,
)

class MATERIAL_UL_extreme_matslot(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        scene = data
        ob = item
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.prop(ob, "name", text="", emboss=False, icon_value=layout.icon(ob))

class ORIGINAL_PT_CreateCameraPass(bpy.types.Panel):

    bl_label ="Create Object Camera"
    bl_space_type = "VIEW_3D"
    bl_region_type ="UI"
    bl_category = "CameraPass"
    bl_context = "objectmode"

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon="PLUGIN")

    def draw(self, context):
        layout = self.layout
        layout.operator(create_camera_pass.ORIGINAL_OT_CreateCameraPass.bl_idname, text="Create Camera Pass")
        
        box = layout.box()
        box.label(text="Target objects")

        scn = context.scene
        layout = self.layout
        col = layout.column()
        col.template_list(
            "MATERIAL_UL_extreme_matslot",
            "",
            scn,
            "objects",
            scn,
            "active_object_index")
        

classes = [
    ORIGINAL_PT_CreateCameraPass,
    create_camera_pass.ORIGINAL_OT_CreateCameraPass,
    MATERIAL_UL_extreme_matslot,
]


# ------------------------------------------------------------------------
# register and unregister functions
# ------------------------------------------------------------------------

def register():
    bpy.types.Scene.active_object_index = IntProperty()
    for c in classes:
        bpy.utils.register_class(c)
    print("START")

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    del bpy.types.Scene.active_object_index
    print("REMOVED")

if __name__=="__main__":
    register()
