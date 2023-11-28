import operations.matricial as mat

class cameramanager:
    def __init__(self, camerasettings) -> None:
        self.settings = camerasettings
        
    def screencoordinates(self, P, screenresx, screenresy):
        normalizecoordinatepoints = self.normalizecoordinates(P) # xsnormalized[0] ysnormalizes[1]
        i = (normalizecoordinatepoints[0]+1)/2 * screenresx + 0.5
        j = screenresy - (normalizecoordinatepoints[1]+1/2) * screenresy + 0.5
        return [int(i), int(j)]
        
    def normalizecoordinates(self, P):
        perspectiveviewpoints = self.perspectiveview(P) # xs[0] ys[1]
        normalizedxs = perspectiveviewpoints[0]/self.settings["hx"][0]
        normalizedys = perspectiveviewpoints[1]/self.settings["hy"][0]
        return [normalizedxs, normalizedys]
        
    def perspectiveview(self, P):
        viewcoorinatepoints = self.viewcoordinates(P) # x[0] y[1] z[2]
        xs = self.settings["d"][0] * (viewcoorinatepoints[0]/viewcoorinatepoints[2])
        ys = self.settings["d"][0] * (viewcoorinatepoints[1]/viewcoorinatepoints[2])
        return [xs, ys]
        
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