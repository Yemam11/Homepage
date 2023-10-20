import aspose.threed as a3d


def threeds_to_glb(path):
    input = path
    scene = a3d.Scene.from_file(input)
    scene.save("3D Models\hest.glb")


def glb_to_usdz(path):
    input = path
    scene = a3d.Scene.from_file(input)
    scene.save("3D Models\cubetexture.usdz")

threeds_to_glb("3D Models\hest.3ds")

#TODO: find some way to make the names change with successive file uploads/standardize the naming of the output files