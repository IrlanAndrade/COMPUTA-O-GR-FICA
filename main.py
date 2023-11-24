import files.loadfile as lf
import files.filepath as fp
import pygame

pygame.init()

black       = (0, 0, 0)
window_size = (400, 300)
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
                print(f"Camera: {camerasettings}")

pygame.quit()