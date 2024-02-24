import operations.matricial as mat

class cameramanager:
    def __init__(self, camerasettings) -> None:
        self.settings = camerasettings
        self.oldandnewvertices = []
        
    def screencoordinates(self, P, screenresx, screenresy):
        normalizecoordinatepoints = self.normalizecoordinates(P) # xsnormalized[0] ysnormalizes[1]
        i = (((normalizecoordinatepoints[0]+1)/2) * screenresx) + 0.5
        j = screenresy - (((normalizecoordinatepoints[1]+1)/2) * screenresy) + 0.5
        
        newvertice = [int(i), int(j), int(normalizecoordinatepoints[2])]
        oldvertice = P
        self.oldandnewvertices.append([newvertice, oldvertice])
        
        return [int(i), int(j), int(normalizecoordinatepoints[2])]
        
    def normalizecoordinates(self, P):
        perspectiveviewpoints = self.perspectiveview(P) # xs[0] ys[1]
        normalizedxs = perspectiveviewpoints[0]/self.settings["hx"][0]
        normalizedys = perspectiveviewpoints[1]/self.settings["hy"][0]
        return [normalizedxs, normalizedys, perspectiveviewpoints[2]]
        
    def perspectiveview(self, P):
        viewcoorinatepoints = self.viewcoordinates(P) # x[0] y[1] z[2]
        xs = self.settings["d"][0] * (viewcoorinatepoints[0]/viewcoorinatepoints[2])
        ys = self.settings["d"][0] * (viewcoorinatepoints[1]/viewcoorinatepoints[2])
        return [xs, ys, viewcoorinatepoints[2]]
        
    def viewcoordinates(self, P):
        Vnew = self.orthogonalization()
        U    = self.findU(Vnew)
        normaN, normaV, normaU = self.norma(self.settings["N"]), self.norma(Vnew), self.norma(U)
        basechangematrix       = [normaU, normaV, normaN]
        
        return mat.productmatrixbyvetor(basechangematrix, mat.matrixsub([P], [self.settings["C"]]))
    
    def orthogonalization(self):
        V = self.settings["V"]
        N = self.settings["N"]
        
        Vnew = mat.scalarprojection(V,N)/mat.scalarprojection(N,N)
        Vnew = mat.scalarproduct([N], Vnew)
        Vnew = mat.matrixsub([V], Vnew)
        
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
    
    def facenormal(self, triangulo):
        v1, v2, v3 = triangulo
        v2subv1 = mat.matrixsub([v2], [v1])
        v3subv1 = mat.matrixsub([v3], [v1])
        
        N = mat.vetorialproduct(v2subv1, v3subv1)
        
        N_ = self.normalization(N)
        
        Nnormal = []
        for value in N:
            Nnormal.append(value/self.normalization(N))
        return Nnormal
    
    def verticenormal(self, vertice):
        pass
