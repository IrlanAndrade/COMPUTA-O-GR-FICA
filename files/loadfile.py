def loadfile(filepath):
    with open(filepath, 'r') as file:
        file = file.readlines()
        
    filecontent = {
        "Nvertices":  0,
        "Ntriangles": 0,
        "XYZverticescoords":  [],
        "XYZtrianglescoords": []
    }
    
    content = list(filecontent.items())
    for i, value in enumerate(file):
        readline = value.split()
        if i == 0: filecontent["Nvertices"], filecontent["Ntriangles"] = int(readline[0]), int(readline[1])
        elif i <= filecontent["Nvertices"]: filecontent["XYZverticescoords"].append([float(n) for n in value.split()])
        else: filecontent["XYZtrianglescoords"].append([float(n) for n in value.split()])
        
    return filecontent
        
def loadcamera(filepath):
    with open(filepath, 'r') as file:
        file = file.readlines()
        
    camerasettings = {
        "N":  [],
        "V":  [],
        "d":  [],
        "hx": [],
        "hy": [],
        "C":  [],
    }
    
    settings = list(camerasettings.items())
    for i, value in enumerate(file):
        camerasettings[settings[i][0]] = [float(n) for n in value.split()]
            
    return camerasettings