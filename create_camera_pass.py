import bpy
from mathutils import *
import numpy as np
import random

class ORIGINAL_OT_CreateCameraPass(bpy.types.Operator):

    bl_idname ="camera.create_camera_pass"
    bl_label = "Create Passed Camera"
    bl_description = "Add Pass and Camera"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Vector 生成
        def createVector(object):
            vec_r = min(object.scale[0], object.scale[1], object.scale[2]) * random.uniform(1.0, 3.0)
            vec_theta = random.uniform(0.0, np.pi)
            vec_phi = random.uniform(0.0, 2.0*np.pi-0.0001)
            vec_co = Vector(
                (vec_r*np.sin(vec_theta)*np.cos(vec_phi),
                vec_r*np.sin(vec_theta)*np.sin(vec_phi),
                vec_r*np.cos(vec_theta)))
            return vec_co

        # ===========================================
        #
        # Create new Collection
        #
        newCol = bpy.data.collections.new('Scene')
        # アクティブコレクションをnewColに設定
        bpy.context.scene.collection.children.link(newCol)

        # 選択オブジェクト
        selected_obj = context.selected_objects

        #
        # Create Camera
        #
        camera_data = bpy.data.cameras.new(name='Camera')
        camera_obj = bpy.data.objects.new("Camera", camera_data)
        newCol.objects.link(camera_obj)

        #
        # Create curve
        #
        # camera pass
        camera_pass_data = bpy.data.curves.new("Camera_pass", type='CURVE')    
        camera_pass_data.dimensions = '3D'    
        camera_pass_obj = camera_pass_data.splines.new('BEZIER')
        camera_pass_obj.bezier_points.add(len(selected_obj)-1)    # 制御点数ー１個

        # camera target_pass pass
        target_pass_data = bpy.data.curves.new("Target_pass", type='CURVE')    
        target_pass_data.dimensions = '3D'    
        target_pass_obj = target_pass_data.splines.new('BEZIER')
        target_pass_obj.bezier_points.add(len(selected_obj)-1) 

        vec1 = Vector((-1, -1, -1))
        vec2 = Vector((1, 1, 1))
        cnt = 0
        for p in selected_obj:
            vec_co = createVector(p)
            camera_pass_obj.bezier_points[cnt].co = p.location + vec_co
            camera_pass_obj.bezier_points[cnt].handle_left = p.location + vec_co + vec1
            camera_pass_obj.bezier_points[cnt].handle_right = p.location +vec_co + vec2
            
            target_pass_obj.bezier_points[cnt].co = p.location 
            target_pass_obj.bezier_points[cnt].handle_left = p.location + vec1
            target_pass_obj.bezier_points[cnt].handle_right = p.location + vec2
            cnt += 1

        #
        # 各オブジェクトの追加
        #
        camera_pass_obj = bpy.data.objects.new("Camera_pass", camera_pass_data) 
        newCol.objects.link(camera_pass_obj)    # コレクションにcurveをリンク

        target_pass_obj = bpy.data.objects.new("target_pass", target_pass_data) 
        newCol.objects.link(target_pass_obj)

        # カメラの注視点をオブジェクトに設定, アクティブカメラに設定
        target_obj = bpy.data.objects.new("target_object", None) # empty
        newCol.objects.link(target_obj)

        #
        # コンストラクタの設定
        #
        # カメラをカーブに追従
        camera_follow_constraint = camera_obj.constraints.new(type='FOLLOW_PATH')
        camera_follow_constraint.target = camera_pass_obj
        camera_follow_constraint.use_fixed_location = True

        # frame_num = 0
        # bpy.context.scene.frame_set(frame_num)
        # camera_follow_constraint.offset.keyframe_insert()
        


        # カメラの注視点をemptyに設定
        camera_target_constraint = camera_obj.constraints.new(type='TRACK_TO')
        camera_target_constraint.target = target_obj
        

        print(camera_target_constraint)
        print("bbb")

        # target object(empty)のコンストラクタ
        target_follow_constraint = target_obj.constraints.new(type='FOLLOW_PATH')
        target_follow_constraint.target = target_pass_obj
        target_follow_constraint.use_fixed_location  = True
        

        # コンストレイントの各種設定
        # パスアニメーション
        
        print("Camera created.")
        return {'FINISHED'}