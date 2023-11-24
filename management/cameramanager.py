import operations.matricial as mat

class cameramanager:
    def __init__(self, camerasettings) -> None:
        self.settings = camerasettings
        
    def viewcoordinates(self):
        Vnew = self.orthogonalization()
        U    = self.findU(Vnew)
        
        normaN = self.norma(self.settings["N"])
        normaV = self.norma(Vnew)
        normaU = self.norma(U)
        
        return [normaU, normaV, normaN]
    
    def orthogonalization(self):
        V = self.settings["V"]
        N = self.settings["N"]
        
        Vnew = mat.scalarprojection(V,N)/mat.scalarprojection(N,N)
        Vnew = mat.scalarproduct(N, Vnew)
        Vnew = mat.matrixsub(V, Vnew)
        
        return Vnew
    
    def findU(self, Vnew):
        return mat.vetorialproduct(self.settings["N"], Vnew)
    
    def normalization(self, matrix):
        
        if len(matrix) != 3:
            mat = []
            for a in matrix: mat.extend(a)
        else: mat = matrix
        
        squaresum = 0
        for value in mat:
            squaresum += value**2
        norma = squaresum**0.5
        
        return norma
    
    def norma(self, matrix):
        
        if len(matrix) != 3:
            mat = []
            for a in matrix: mat.extend(a)
        else: mat = matrix
        
        newmatrix = []
        for value in mat:
            newmatrix.append(value/self.normalization(mat))
            
        return newmatrix
    
camerasettings = {
        "N":  [-1,-1,-1],
        "V":  [0,0,1],
        "d":  1,
        "hx": 1,
        "hy": 1,
        "C":  [1,1,2],
    }

                    
    
    