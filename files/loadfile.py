def loadfile(filepath):
    with open(filepath, 'r') as file:
        return file.read()
        
def loadcamera(filepath):
    with open(filepath, 'r') as file:
        file = file.readlines()
        
    camerasettings = {
        "N":  [],
        "V":  [],
        "d":  0,
        "hx": 0,
        "hy": 0,
        "C":  [],
    }
    
    settings = list(camerasettings.items())
    for i, value in enumerate(file):
        camerasettings[settings[i][0]] = [float(n) for n in value.split()]
            
    return camerasettings