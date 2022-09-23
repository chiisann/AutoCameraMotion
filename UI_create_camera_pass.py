import bpy
from . import create_camera_pass

class ORIGINAL_PT_CreateCameraPass(bpy.types.Panel):

    bl_label ="Create Object Camera"
    bl_space_type = "VIEW_3D"
    bl_region_type ="UI"
    bl_category = "CameraPass"
    bl_context = "objectmode"

    # オブジェクト選択時にメニューを表示
    # def poll(cls, context):
    #     # return True
    #     for o in bpy.data.objects:
    #         if o.select_get():
    #             return True
    #     return False
    
    # def draw_header(self, context):
    #     layout = self.layout
    #     layout.label(text="", icon="PLUGIN")
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="button")
        # layout.operator(create_camera_pass.ORIGINAL_OT_CreateCameraPass.bl_idname, text="Create Camera Pass")

