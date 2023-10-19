import aspose.threed as a3d


def stp_to_glb(path):
    input = path
    scene = a3d.Scene.from_file(input)
    scene.save("output.glb")


def stl_to_usdz(path):
    input = path
    scene = a3d.Scene.from_file(input)
    scene.save("output.usdz")

def glb_to_usdz(path):
    input = path
    scene = a3d.Scene.from_file(input)
    scene.save("testbillet.usdz")

def glb_to_stl(path):
    input = path
    scene = a3d.Scene.from_file(input)
    scene.save("testing.stl")


glb_to_usdz("Test-Billet_Tiger-Tool.glb")

#TODO: find some way to make the names change with successive file uploads/standardize the naming of the output files