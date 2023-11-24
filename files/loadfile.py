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
    
    for i, f in enumerate(file): # Para cada linha
        aux, value = [], ""
        for string in f: # Para cada letra na linha
            if string == " " or string == "\n":
                aux.append(int(value))
                value = ""
            else: value += string
        camerasettings[settings[i][0]] = aux[0] if aux[-1] == aux[0] else [int(x) for x in aux]
        
    return camerasettings

def writecamera(filepath, camerasettings):
    settings = list(camerasettings.items())
    
    with open(filepath, 'w') as file:
        aux = []
        for setting in settings: # Para cada item em settings 
            aux.append(setting[1]) # Pegue apenas o valor
        for setting in aux: # Para cada valor separado tal que [1, 2, ..., n] pegue cada valor separado até n
            if isinstance(setting, int): file.write(str(setting) + "\n")
            else: 
                for i, set in enumerate(setting):
                    if i == len(setting) -1: file.write(str(set) + "\n")
                    else: file.write(str(set) + " ")