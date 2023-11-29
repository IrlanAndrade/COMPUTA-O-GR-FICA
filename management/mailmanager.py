import pygame
from time import sleep

class mailmanager:
    def __init__(self, object3d) -> None:
        self.object3d = object3d
        
    def drawpixel(self, x, y, screen):
        screen.set_at((x, y), (255, 255, 255))
        sleep(0.005)
    
    def drawline(self, x0, y0, x1, y1, screen):
        deltax = abs(x1 - x0)
        deltay = abs(y1 - y0)

        error = deltax - deltay

        x, y = x0, y0

        while x != x1 and y != y1:
            deltaerror = 2 * error
            if deltaerror > -deltay:
                error -= deltay
                if x0 < x1: x += 1
                else: x-= 1
            if deltaerror < deltax:
                error += deltax
                if y0 < y1: y += 1 
                else: y -= 1

            screen.set_at((x, y), (255, 255, 255))
            sleep(0.000001)
        
            