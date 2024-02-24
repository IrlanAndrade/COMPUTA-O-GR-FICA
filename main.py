import pygame
import files.filepath as fp
import files.loadfile as lf
import operations.matricial as mat
from management import cameramanager as cmanager
from management import mailmanager as mmanager
from time import sleep

def drawpixel(m, screen, animate):
    for i in range(m.object3d["Nvertices"]):
        x, y, _ = c.screencoordinates(m.object3d["XYZverticescoords"][i], window_size[0], window_size[1])
        m.drawpixel(x, y, screen)
        if animate:
            sleep(0.005)
            pygame.display.flip()
        
def drawline(c, m, screen, animate):
    indextriangle = m.object3d["indextriangles"]
    for trianglelist in range(m.object3d["Ntriangles"]): # percorre cada listas de indices
        for verticeslist in range(len(indextriangle[0])): # percorre cada indice na listas de indices vigente
            actualverticeslist     = indextriangle[trianglelist]
            actualvertice          = int(actualverticeslist[verticeslist]) - 1
            
            if (verticeslist + 1) % len(indextriangle[0]) == 0: nextvertice = int(actualverticeslist[verticeslist % (len(indextriangle[0])-1)]) - 1
            else: nextvertice = int(actualverticeslist[verticeslist+1]) - 1
                
            x0, y0, z0 = c.screencoordinates(m.object3d["XYZverticescoords"][actualvertice], window_size[0], window_size[1])
            x1, y1, z1 = c.screencoordinates(m.object3d["XYZverticescoords"][nextvertice], window_size[0], window_size[1])
            m.drawline(x0,y0,z0, x1,y1,z1, screen, True)
            if animate:
                sleep(0.0005)
                pygame.display.flip()
            
def scanline(c, m, screen, animate):
    indextriangle = m.object3d["indextriangles"]
    for trianglelist in range(m.object3d["Ntriangles"]): # percorre cada listas de indices
        verticestoorder = []
        for verticeslist in range(len(indextriangle[0])): # percorre cada indice na listas de indices vigente
            actualverticeslist     = indextriangle[trianglelist]    
            actualvertice          = int(actualverticeslist[verticeslist]) - 1
            x, y, z = c.screencoordinates(m.object3d["XYZverticescoords"][actualvertice], window_size[0], window_size[1])
            verticestoorder.append([x, y, z])
        m.scanline(verticestoorder, screen)
        if animate:
            sleep(0.005)
            pygame.display.flip()
            
def getVertices(m):
    indextriangle = m.object3d["indextriangles"]
    verticesintrianglelist = []
    for trianglelist in range(m.object3d["Ntriangles"]): # percorre cada listas de indices
        for verticeslist in range(len(indextriangle[0])): # percorre cada indice na listas de indices vigente
            actualverticeslist     = indextriangle[trianglelist]    
            actualvertice          = int(actualverticeslist[verticeslist]) - 1
            
            verticesintrianglelist.append(m.object3d["XYZverticescoords"][actualvertice])
    return verticesintrianglelist

def getFacesByVertices(m:mmanager.mailmanager, c:cmanager.cameramanager, vertice):
    oldvertice = None
    for v in c.oldandnewvertices:
        # print(f"v[0]: {v[0]}")
        if v[0] == vertice: oldvertice = v[1]
        
    verticeindex = 0
    for v in m.object3d["XYZverticescoords"]:
        if [int(valor) for valor in v] == [int(valor) for valor in oldvertice]: break
        verticeindex += 1
    
    adjascentsfaces = []
    for faces in m.object3d['indextriangles']:
        for verticeposition in faces:
            if verticeposition == verticeindex + 1: adjascentsfaces.append((faces))
    
    adjvertices = []
    for indexes in adjascentsfaces:
        aux = []
        for index in indexes:
            # print(f"index: {index}")
            aux.append(m.object3d['XYZverticescoords'][int(index)-1])
        adjvertices.append(aux)
        
    # print(adjvertices)
    
    newadjvertices = []
    for vertices in adjvertices:
        aux = []
        # print(f"vertices: {vertices}")
        for v in vertices:
            # print(f"v: {v}")
            for oldnew in c.oldandnewvertices:
                # print(f"oldnew: {oldnew}")
                if [int(valor) for valor in v] == [int(valor) for valor in oldnew[1]]: 
                    aux.append([int(valor) for valor in oldnew[0]])
                    # print(f"aux: {aux}")
        newadjvertices.append([aux])
     
    # print(f"newadjvertices {newadjvertices}")   
       
    
    Nface = [[0,0,0]]
    for adjvertices in newadjvertices:
        # print(f"adjvertices {adjvertices}")
        for vertices in adjvertices:
            vertices = {frozenset(l) for l in vertices}
            vertices = set(vertices)
            vertices = [list(frozenset) for frozenset in vertices]
            print(f"Nface: {Nface}")
            
            Nface = mat.matrixsum(Nface, [c.facenormal(vertices)])
            
    Nvertice = mat.scalarproduct(Nface, 1/3) 
    
    Nverticenormal = []
    for value in Nvertice[0]:
        Nverticenormal.append(value/c.normalization(Nvertice))
    
    return Nverticenormal 
    
    
     
black       = (0, 0, 0)
window_size = (720, 720)
screen      = pygame.display.set_mode(window_size)     
        
camerasettings = lf.loadcamera(fp.filepath()["camerapath"]) # Carrega novamente os parametros da camera
objectsettings = lf.loadfile(fp.filepath()["calice2"]) 
c              = cmanager.cameramanager(camerasettings)
m              = mmanager.mailmanager(objectsettings)
m.createzbuffer(window_size)
        
            
pygame.init()

pygame.display.set_caption('OBJECTS 3D VIEWER')
screen.fill(black)
        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:  # Verifica se uma tecla foi pressionada
            if event.key == pygame.K_r:  # Recarrega
                screen.fill(black)
                
                text = input()
                if text != "": objectsettings = lf.loadfile(fp.filepath()[text])
                camerasettings = lf.loadcamera(fp.filepath()["camerapath"]) # Carrega novamente os parametros da camera
                                
                c = cmanager.cameramanager(camerasettings)
                m = mmanager.mailmanager(objectsettings)
                m.createzbuffer(window_size)
                drawpixel(m, screen, False)
                drawline(c, m, screen, False)
                scanline(c, m, screen, False)
                
            if event.key == pygame.K_s: # Apenas mostra
                screen.fill(black)
                # drawpixel(m, screen, False)
                # drawline(c, m, screen, False)
                scanline(c, m, screen, False)
                for vertice in c.oldandnewvertices:
                    print(vertice)
                
            if event.key == pygame.K_a: # Mostra Animado
                screen.fill(black)
                # drawpixel(m, screen, True)
                # drawline(c, m, screen, True)
                scanline(c, m, screen, True)
                
            if event.key == pygame.K_z:
                scanline(c, m, screen, False)
                print(getFacesByVertices(m, c, [296, 525, 865]))
                pass
                
            if event.key == pygame.K_c: # Apaga o desenho atual
                screen.fill(black)
                    
    pygame.display.flip()
pygame.quit()
