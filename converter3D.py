import aspose.threed as a3d


def stl_to_glb(path):
    input = path
    scene = a3d.Scene.from_file(input)
    scene.save("3D Models\texturedcube.glb")


def stl_to_usdz(path):
    input = path
    scene = a3d.Scene.from_file(input)
    scene.save("output.usdz")

def glb_to_usdz(path):
    input = path
    scene = a3d.Scene.from_file(input)
    scene.save("3D Models\cube.usdz")

def glb_to_stl(path):
    input = path
    scene = a3d.Scene.from_file(input)
    scene.save("3D Models\testing.stl")


stl_to_glb("3D Models\texturedcube.stl")

#TODO: find some way to make the names change with successive file uploads/standardize the naming of the output files