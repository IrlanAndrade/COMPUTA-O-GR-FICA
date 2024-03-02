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
        # print(f"T: {triangulo}")
        v1, v2, v3 = triangulo
        # print(v1, v2, v3)
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
    
    def getVertices(m):
        indextriangle = m.object3d["indextriangles"]
        verticesintrianglelist = []
        for trianglelist in range(m.object3d["Ntriangles"]): # percorre cada listas de indices
            for verticeslist in range(len(indextriangle[0])): # percorre cada indice na listas de indices vigente
                actualverticeslist     = indextriangle[trianglelist]    
                actualvertice          = int(actualverticeslist[verticeslist]) - 1
                
                verticesintrianglelist.append(m.object3d["XYZverticescoords"][actualvertice])
        return verticesintrianglelist

    def remover_duplicatas(self, lista_de_listas): #AUX
        # Usar um conjunto para manter as tuplas únicas
        conjunto_unico = set()

        # Lista resultante sem duplicatas
        lista_sem_duplicatas = []

        for lista in lista_de_listas:
            # Convertendo a lista interna em uma tupla
            tupla_da_lista = tuple(lista)

            # Verificando se a tupla já está no conjunto
            if tupla_da_lista not in conjunto_unico:
                # Adicionando a tupla única à lista resultante
                lista_sem_duplicatas.append(lista)
                
                # Adicionando a tupla ao conjunto para evitar duplicatas
                conjunto_unico.add(tupla_da_lista)

        return lista_sem_duplicatas

    def getFacesByVertices(self, m, vertice): # 
        # print(f"vertice {vertice}")
        # print(f"oldnew: {self.oldandnewvertices}")
        oldvertice = None
        for v in self.oldandnewvertices:
            # print(f"v[0]: {v[0]}")
            if v[0] == vertice: 
                oldvertice = v[1]
        # print(vertice)
            
        # print(oldvertice)
            
        verticeindex = 0
        for v in m.object3d["XYZverticescoords"]:
            if [int(valor) for valor in v] == [int(valor) for valor in oldvertice]: break
            # #print(valor1)
            verticeindex += 1
        
        adjascentsfaces = []
        for faces in m.object3d['indextriangles']:
            for verticeposition in faces:
                if verticeposition == verticeindex + 1: adjascentsfaces.append((faces))
        
        adjvertices = []
        for indexes in adjascentsfaces:
            aux = []
            for index in indexes:
                # #print(f"index: {index}")
                aux.append(m.object3d['XYZverticescoords'][int(index)-1])
            adjvertices.append(aux)
        
        # print(f"vertices {adjvertices}")
        
        newadjvertices = []
        for vertices in adjvertices:
            aux = []
            for v in vertices:
                # print(f"v: {v}")
                for oldnew in self.oldandnewvertices:
                    # print(f"oldnew: {oldnew[1]}")
                    if v == oldnew[1]: 
                        aux.append([int(valor) for valor in oldnew[0]])
            # print(f"aux: {aux}")
            newadjvertices.append([aux])
        
        # print(f"newadjvertices {newadjvertices}")
        
        Nface = [[0,0,0]]
        for adjvertices in newadjvertices:
            # print(f"adjvertices {adjvertices}")
            for vertices in adjvertices:
                # if len(vertices) != 3: print(vertices)
                vertices = self.remover_duplicatas(vertices)
                # vertices = {frozenset(l) for l in vertices}
                # vertices = set(vertices)
                # vertices = [list(frozenset) for frozenset in vertices]
                # print(f"vertices: {vertices}")
                Nface = mat.matrixsum(Nface, [self.facenormal(vertices)])
                
        Nvertice = mat.scalarproduct(Nface, 1/3) 
        
        Nverticenormal = []
        for value in Nvertice[0]:
            Nverticenormal.append(value/self.normalization(Nvertice))
        
        return Nverticenormal 
    
    def getDirectLight(self, vertice):
        lightposition = self.settings['Pl']
        #print(f"lightposition {lightposition}")
        #print(f"vertice {vertice}")
        
        L = mat.matrixsub([lightposition], [vertice])
        #print(f"L {L}")
        
        Lnormal = []
        for value in L[0]:
            Lnormal.append(value/self.normalization(L))
        
        return Lnormal
    
    def getReflecion(self, m, vertice):
        lightposition = self.settings['Pl']
        N = self.getFacesByVertices(m, vertice)
        R = mat.scalarprojection(lightposition, N)
        #print(f"R: {R}")
        #print(f"N {N} | 2*R {2*R}")
        R = mat.scalarproduct([N], (2 * R))
        #print(f"R: {R}")
        L = self.getDirectLight(vertice)
        #print(f"L: {L}")
        R = mat.matrixsub([L], R)
        #print(f"R: {R}")
        
        return R
        
    def getDirectViewer(self, vertice):
        cameraposition = self.settings['C']
        #print(f"cameraposition {cameraposition}")
        #print(f"vertice {vertice}")
        
        V = mat.matrixsub([cameraposition], [vertice])
        #print(f"V {V}")
        
        Lnormal = []
        for value in V[0]:
            Lnormal.append(value/self.normalization(V))
        
        return Lnormal
        
    def totalLightIntense(self, m, vertice):
        
        print(f"Para o ponto: {vertice}")
        
        L, Kd, Od, Ks, n, Il, Ka = self.settings['Pl'], self.settings['Kd'], self.settings['Od'], self.settings['Ks'], self.settings['n'], self.settings['Il'], self.settings['Ka']
        #print(f"m {m} | vertice {vertice}")
        N = self.getFacesByVertices(m, vertice)
        R = self.getReflecion(m, vertice)
        V = self.getDirectViewer(vertice)
        Iamb = self.settings['Iamb']
        
        #print(Ka, Iamb)
        Ia = mat.scalarproduct([Iamb], Ka[0])
        # Ia = [x for x in Ia[0]]
        #print(f"Ia {Ia}")
        
        print(f"R: {R[0]}")
        print(f"V: {V}")
        print(f"N: {N}")
        print(f"Ia: {N}")
        
        
        check, N = self.desconsiderLight(V, N, L)
        
        if check == False:
        
            #print(L, N)
            Id = mat.scalarprojection(L, N)
            #print(f"Id: {Id}")
            #print(f"Kd: {Kd}")
            Id = mat.scalarproduct([Kd], Id)
            #print(f"Id: {Id}")
            Id = [x * Od[i] for i, x in enumerate(Id[0])]
            Id = [[x * Il[i] for i, x in enumerate(Id)]]
            print(f"Id: {Id[0]}")
            
            check = self.desconsiderEspecular(V, R)
            
            if check == False:
                #print(R, V)
                Is = mat.scalarprojection(R[0], V)
                #print(Is)
                #print(n)
                Is = Is ** n[0]
                #print(f"Is {Is}")
                #print(f"Ks {Ks}")
                Is = Is * Ks[0]
                #print(f"Il {Il}")
                Is = mat.scalarproduct([Il], Is)
                print(f"Is: {Is}")
                
                I = mat.matrixsum(Ia, Id)
                #print(f"I: {I}")
                I = mat.matrixsum(I, Is)
                
            else: 
                I = mat.matrixsum(Ia, Id)
                print(f"Ie: Desconsiderado")
            
        else: 
            I = Ia
            print(f"Id: Desconsiderado")
            print(f"Ie: Desconsiderado")
            
        #print(f"I: {I}")
        I = [min(x, 255) for x in I[0]]
        print(f"I: {I}")
        
        return I
        
    def desconsiderLight(self, V, N, L,):
        tocheck  = mat.scalarprojection(L, N) 
        tocheck2 = mat.scalarprojection(V, N) 
        #print(f"tc: {tocheck}")
        #print(f"tc2: {tocheck2}")
        if tocheck < 0:
            if tocheck2 < 0:
                #print("False")
                return False, [-x for x in N]
            else:
                #print("True")
                return True, True
        return False, N
            
    def desconsiderEspecular(self, V, R):
        tocheck  = mat.scalarprojection(V, R[0]) 
        if tocheck < 0:
            return True
        return False
    
    # def paintPixel(self, m, vertice, screen):
    #     rgb = self.totalLightIntense(m, vertice)
    #     #print(f"rgb = {rgb}")
    #     x, y = vertice[0], vertice[1]
        
    #     r = rgb[0] if rgb[0] != None else 0
    #     g = rgb[1] if rgb[1] != None else 0
    #     b = rgb[2] if rgb[2] != None else 0
        
    #     screen.set_at((x, y), (r, g, b))
                