import pygame
from time import sleep

class mailmanager:
    def __init__(self, object3d) -> None:
        self.object3d = object3d
        
    def drawpixel(self, x, y, screen):
        screen.set_at((x, y), (255, 255, 255))
        
    def drawline(self, x1, y1, x2, y2, screen):
        deltax = abs(x2 - x1)
        deltay = abs(y2 - y1)

        error = deltax - deltay
        x, y  = x1, y1

        while not (x == x2 and y == y2):
            deltaerror = 2 * error

            if deltaerror > -deltay:
                error -= deltay
                if x1 < x2: x += 1
                else: x -= 1

            if deltaerror < deltax:
                error += deltax
                if y1 < y2: y += 1
                else: y -= 1

            screen.set_at((x, y), (255, 255, 255))