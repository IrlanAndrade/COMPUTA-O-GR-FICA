import files.loadfile as lf
import files.filepath as fp
import management.cameramanager as manager
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
                c = manager.cameramanager(camerasettings)
                
                print(f"Camera: {camerasettings}")
                print(f"Ponto [1,-3,-5] em coordenadas de vista: {c.viewcoordinates([1,-3,-5])}")
                print(f"Informações do objeto: {lf.loadfile(fp.filepath()["triangulo"])}")
                print(f"Ponto [1,-3,-5] em projeção em perspectiva: {c.perspectiveview([1,-3,-5])}")
                print(f"Ponto [1,-3,-5] em coordenadas normalizadas: {c.normalizecoordinates([1,-3,-5])}")
                print(f"Ponto [1,-3,-5] em coordenadas de tela: {c.screencoordinates([1,-3,-5], window_size[0], window_size[1])}")

pygame.quit()