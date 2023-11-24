def scalarprojection(matrixa, matrixb):
    scalar = 0
    for i, value in enumerate(matrixa): 
        scalar += int(value) * matrixb[i] 
        
    return scalar

def scalarproduct(matrix, scalar):
    result, sum = [], 0 
    for value in matrix:
        sum += value * scalar
        result.append(sum)
        sum = 0
        
    return result

def vetorialproduct(matrixa, matrixb):
    mata = tolistinlist(matrixa)
    matb = tolistinlist(matrixb)
        
    result = [
        mata[1] * matb[2] - mata[2] * matb[1],
        mata[2] * matb[0] - mata[0] * matb[2],
        mata[0] * matb[1] - mata[1] * matb[0]
    ]
    
    return result

def matrixmul(matrixa, matrixb):
    mata = tolist(matrixa)
    matb = tolist(matrixb)

    result = [[0 for _ in range(len(matb[0]))] for _ in range(len(mata))]

    for i in range(len(mata)):
        for j in range(len(matb[0])):
            for k in range(len(mata[0])): result[i][j] += mata[i][k] * matb[k][j]

    return result

def matrixsub(matrixa, matrixb):
    mata = tolist(matrixa)
    matb = tolist(matrixb)
    
    result = [[0 for _ in range(len(matb[0]))] for _ in range(len(mata))]

    for i in range(len(mata)):
        for j in range(len(matb[0])): result[i][j] = mata[i][j] - matb[i][j]
        
    return result

# utils
def tolist(matrix): # [[]],[[]] --> [],[]
    if all(isinstance(sublist, list)for sublist in matrix) == False:
        mat = []
        mat.append(matrix)
    else: mat = matrix
    
    return mat

def tolistinlist(matrix): # [],[] --> [[]],[[]]
    if len(matrix) != 3:
        mat = []
        for value in matrix: mat.extend(value)
    else: mat = matrix
    
    return mat