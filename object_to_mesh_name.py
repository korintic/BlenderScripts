import bpy


def main(context):
    for ob in  context.selected_objects:
        if ob.type == 'MESH':
            if ob.name in bpy.data.meshes:
                _name = bpy.data.meshes[ob.name].name
                bpy.data.meshes[ob.name].name += ".01"
            ob.data.name = ob.name

            

class CopyObjectToMeshName(bpy.types.Operator):
    """Copy object name to mesh name on selected objects"""
    bl_idname = "object.object_to_mesh_name"
    bl_label = "Copy Object to Mesh Name"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(CopyObjectToMeshName)


def unregister():
    bpy.utils.unregister_class(CopyObjectToMeshName)


if __name__ == "__main__":
    register()
