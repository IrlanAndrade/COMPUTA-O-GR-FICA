def scalarprojection(matrixa, matrixb): # []
    scalar = 0
    for i, value in enumerate(matrixa): 
        scalar += value * matrixb[i] 
        
    return scalar

def productmatrixbyvetor(matrixa, vetor): # need [[]]
    result = [0 for _ in range(len(matrixa))]
    
    for i in range(len(matrixa)):
        for j in range(len(vetor[0])):
            result[i] += matrixa[i][j] * vetor[0][j]
    
    return result

def scalarproduct(matrix, scalar): # need [[]] / int scalar
    result, sum = [], 0 
    for i, value in enumerate(matrix):
        aux = []
        for j in matrix[i]:
            sum += j * scalar
            aux.append(sum)
            sum = 0
        result.append(aux)
        
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

def matrixsub(matrixa, matrixb): # need [[]]
    result = [[0 for _ in range(len(matrixb[0]))] for _ in range(len(matrixa))]

    for i, value in enumerate(matrixa):
        for j in range(len(value)):
            result[i][j] = matrixa[i][j] - matrixb[i][j]
        
    return result

def matrixsum(matrixa, matrixb): # need [[]]
    result = [[0 for _ in range(len(matrixb[0]))] for _ in range(len(matrixa))]

    for i, value in enumerate(matrixa):
        for j in range(len(value)):
            result[i][j] = matrixa[i][j] + matrixb[i][j]
        
    return result

def matrixmul(matrixa, matrixb): # need [[]]
    result = [[0 for _ in range(len(matrixb[0]))] for _ in range(len(matrixa))]
    
    for i in range(len(matrixa)):
        for j in range(len(matrixb[0])):
            for k in range(len(matrixb)):
                result[i][j] += matrixa[i][k] * matrixb[k][j]
    
    return result

# utils
def tolistinlist(matrix): # [],[] --> [[]],[[]]
    if len(matrix) != 3:
        mat = []
        for value in matrix: mat.extend(value)
    else: mat = matrix
    
    return mat