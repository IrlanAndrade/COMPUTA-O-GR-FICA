import pygame

class mailmanager:
    def __init__(self, object3d) -> None:
        self.object3d = object3d
        
    def drawpixel(self, x, y, screen):
        screen.set_at((x, y), (255, 255, 255))
    
    def drawline(self, x0, y0, x1, y1, screen):

        deltax = abs(x1 - x0)
        deltay = abs(y1 - y0)

        if x0 < x1: sx = 1
        else: sx = -1
        if y0 < y1: sy = 1
        else: sy = -1

        erro = deltax - deltay

        x, y = x0, y0

        while True:

            if x == x1 and y == y1: break

            erro2 = 2 * erro

            if erro2 > -deltay:
                erro -= deltay
                x += sx

            if erro2 < deltax:
                erro += deltax
                y += sy

            screen.set_at((x, y), (255, 255, 255))
        
            