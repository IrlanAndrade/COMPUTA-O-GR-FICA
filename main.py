import files.loadfile as lf
import files.filepath as fp
import management.cameramanager as cmanager
import management.mailmanager as mmanager
import pygame

pygame.init()

black       = (0, 0, 0)
window_size = (800, 600)
screen      = pygame.display.set_mode(window_size)

pygame.display.set_caption('OBJECTS 3D VIEWER')
screen.fill(black)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:  # Verifica se uma tecla foi pressionada
            if event.key == pygame.K_r:  # Verifica se a tecla é a tecla R
                camerasettings = lf.loadcamera(fp.filepath()["camerapath"]) # Carrega novamente os parametros da camera
                objectsettings = lf.loadfile(fp.filepath()["maca"])
                
                c = cmanager.cameramanager(camerasettings)
                m = mmanager.mailmanager(objectsettings)
                
                for i in range(m.object3d["Nvertices"]):
                    x, y = c.screencoordinates(m.object3d["XYZverticescoords"][i], window_size[0], window_size[1])
                    m.drawpixel(x, y, screen)
                    pygame.display.flip()
                

                for i in m.object3d["indextriangles"]:
                    for enum,j in enumerate(i):
                        index = int(i[enum])-1 # retorna o valor do index ao se acessas index = intextriangles[enum]
                        try:
                            x0, y0 = c.screencoordinates(m.object3d["XYZverticescoords"][int(i[enum])-1], window_size[0], window_size[1])
                            x1, y1 = c.screencoordinates(m.object3d["XYZverticescoords"][int(i[enum+1])-1], window_size[0], window_size[1])
                            m.drawline(x0, y0, x1, y1, screen)
                        except:
                            try:
                                x0, y0 = c.screencoordinates(m.object3d["XYZverticescoords"][int(i[enum])-1], window_size[0], window_size[1])
                                x1, y1 = c.screencoordinates(m.object3d["XYZverticescoords"][int(i[0])], window_size[0], window_size[1])
                                m.drawline(x0, y0, x1, y1, screen)
                            except: pass
                        pygame.display.flip()
pygame.quit()