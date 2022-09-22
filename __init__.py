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

def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(create_camera_pass.ORIGINAL_OT_CreateCameraPass.bl_idname)

classes = [
    create_camera_pass.ORIGINAL_OT_CreateCameraPass,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    print("START")

def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)
        print("REMOVED")

if __name__=="__main__":
    register()
