def scalarprojection(matrixa, matrixb): # []
    scalar = 0
    for i, value in enumerate(matrixa): 
        scalar += int(value) * matrixb[i] 
        
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

def matrixmul(matrixa, matrixb): # need [[]]
    result = [[0 for _ in range(len(matrixb[0]))] for _ in range(len(matrixa))]
    
    for i in range(len(matrixa)):
        for j in range(len(matrixb[0])):
            for k in range(len(matrixb)):
                result[i][j] += matrixa[i][k] * matrixb[k][j]
    
    return result

# def matrixident(n):
#     return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# def matrixdiv(matrixa, matrixb): # need [[]]
#     invb = inverse(matrixb)
    
#     if invb is not None:
#         return matrixmul(matrixa, invb)
#     else:
#         return None

# def inverse(matrix): # need [[]]
#     n = len(matrix)

#     identity = matrixident(n)
#     temp = [line[:] for line in matrix]

#     for col in range(n):
#         max_index = max(range(col, n), key=lambda i: abs(temp[i][col]))
#         if max_index != col:
#             temp[col], temp[max_index] = temp[max_index], temp[col]
#             identity[col], identity[max_index] = identity[max_index], identity[col]

#         for i in range(col + 1, n):
#             coef = -temp[i][col] / temp[col][col]
#             for j in range(col, n):
#                 temp[i][j] += coef * temp[col][j]
#                 identity[i][j] += coef * identity[col][j]

#     for col in range(n - 1, -1, -1):
#         for row in range(col - 1, -1, -1):
#             coef = -temp[row][col] / temp[col][col]
#             for j in range(n - 1, -1, -1):
#                 temp[row][j] += coef * temp[col][j]
#                 identity[row][j] += coef * identity[col][j]

#     for i in range(n):
#         diagonal = temp[i][i]
#         for j in range(n):
#             identity[i][j] /= diagonal

#     return identity

# utils
def tolistinlist(matrix): # [],[] --> [[]],[[]]
    if len(matrix) != 3:
        mat = []
        for value in matrix: mat.extend(value)
    else: mat = matrix
    
    return mat

# matrixa = [
#     [4, 7, 2],
#     [2, 6, 1],
#     [3, 8, 5]
# ]

# matrixb = [
#     [3, 2, 1],
#     [4, 1, 7],
#     [2, 3, 2]
# ]


# print(matrixdiv(matrixa, matrixb))
# print(scalarproduct(matrixdiv(matrixa, matrixb), 2))
#print(matrixsub2(matrixa, matrixb))