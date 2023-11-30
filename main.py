import files.filepath as fp
import files.loadfile as lf
from management import cameramanager as cmanager
from management import mailmanager as mmanager
import pygame

def drawpixel(m, screen, animate):
    for i in range(m.object3d["Nvertices"]):
        x, y = c.screencoordinates(m.object3d["XYZverticescoords"][i], window_size[0], window_size[1])
        m.drawpixel(x, y, screen)
        if animate: pygame.display.flip()
        
def drawline(c, m, screen, animate):
    indextriangle = m.object3d["indextriangles"]
    for trianglelist in range(m.object3d["Ntriangles"]): # percorre cada listas de indices
        for verticeslist in range(len(indextriangle[0])): # percorre cada indice na listas de indices vigente
            actualverticeslist     = indextriangle[trianglelist]
            actualvertice          = int(actualverticeslist[verticeslist]) - 1
            
            if (verticeslist + 1) % len(indextriangle[0]) == 0: nextvertice = int(actualverticeslist[verticeslist % (len(indextriangle[0])-1)]) - 1
            else: nextvertice = int(actualverticeslist[verticeslist+1]) - 1
                
            x0, y0 = c.screencoordinates(m.object3d["XYZverticescoords"][actualvertice], window_size[0], window_size[1])
            x1, y1 = c.screencoordinates(m.object3d["XYZverticescoords"][nextvertice], window_size[0], window_size[1])
            m.drawline(x0,y0, x1,y1, screen)
            if animate: pygame.display.flip()
            
pygame.init()

black       = (0, 0, 0)
window_size = (800, 600)
screen      = pygame.display.set_mode(window_size)

pygame.display.set_caption('OBJECTS 3D VIEWER')
screen.fill(black)
        
camerasettings = lf.loadcamera(fp.filepath()["camerapath"]) # Carrega novamente os parametros da camera
objectsettings = lf.loadfile(fp.filepath()["vaso"]) 
c              = cmanager.cameramanager(camerasettings)
m              = mmanager.mailmanager(objectsettings)
        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:  # Verifica se uma tecla foi pressionada
            if event.key == pygame.K_r:  # Recarrega
                screen.fill(black)
                
                camerasettings = lf.loadcamera(fp.filepath()["camerapath"]) # Carrega novamente os parametros da camera
                objectsettings = lf.loadfile(fp.filepath()["calice2"])
                
                c = cmanager.cameramanager(camerasettings)
                m = mmanager.mailmanager(objectsettings)
                
                drawpixel(m, screen, False)
                drawline(c, m, screen, False)
                
            if event.key == pygame.K_s: # Apenas mostra
                screen.fill(black)
                drawpixel(m, screen, False)
                drawline(c, m, screen, False)
                
            if event.key == pygame.K_a: # Mostra Animado
                screen.fill(black)
                drawpixel(m, screen, True)
                drawline(c, m, screen, True)
                
            if event.key == pygame.K_c:
                screen.fill(black)
                    
    pygame.display.flip()
pygame.quit()
