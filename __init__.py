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

classes = [
    ORIGINAL_PT_CreateCameraPass,
    create_camera_pass.ORIGINAL_OT_CreateCameraPass,
]


# ------------------------------------------------------------------------
# register and unregister functions
# ------------------------------------------------------------------------

def register():
    for c in classes:
        bpy.utils.register_class(c)
    print("START")

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
        print("REMOVED")

if __name__=="__main__":
    register()
