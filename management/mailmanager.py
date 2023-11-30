import pygame
from time import sleep

class mailmanager:
    def __init__(self, object3d) -> None:
        self.object3d = object3d
        
    def drawpixel(self, x, y, screen):
        screen.set_at((x, y), (255, 255, 255))
        
    def drawline(self, x0, y0, x1, y1, screen, draw=True):
        deltax = abs(x1 - x0)
        deltay = abs(y1 - y0)

        list = []

        error = deltax - deltay
        x, y  = x0, y0

        while not (x == x1 and y == y1):
            deltaerror = 2 * error

            if deltaerror > -deltay:
                error -= deltay
                if x0 < x1: x += 1
                else: x -= 1

            if deltaerror < deltax:
                error += deltax
                if y0 < y1: y += 1
                else: y -= 1

            list.append([x, y])

            if draw == True: screen.set_at((x, y), (255, 255, 255))
            
        return list
            
    def scanline(self, vertices, screen):
        vertices.sort(key=lambda y: y[1])
        high   = vertices[0]
        medium = vertices[1]
        low    = vertices[2]
        
        hightriangle = self.drawline(high[0], high[1], medium[0], medium[1], screen, False)
        lowtriangle  = self.drawline(high[0], high[1], low[0], low[1], screen, False)
        
        for y, point in enumerate(lowtriangle):
            if point[1] == medium[1]: 
                hightriangle = [[high[0], high[1]], [point[0], point[1]], [medium[0], medium[1]]]
                lowtriangle  = [[medium[0], medium[1]],[point[0], point[1]], [low[0], low[1]]]
        
        print(f"TRIANGULO ORIGINAL: {vertices}")
        print(f"TRIANGULO SUPERIOR: {hightriangle}")
        print(f"TRIANGULO INFERIOR: {lowtriangle}")

        #Percorre as arestas adjascentes do vértice superior ao inferior
        
        hightriangleright = self.drawline(hightriangle[0][0], hightriangle[0][1], hightriangle[2][0], hightriangle[2][1], screen, False)
        hightriangleleft  = self.drawline(hightriangle[0][0], hightriangle[0][1], hightriangle[1][0], hightriangle[1][1], screen, False)

        #Percorre as arestas adjascentes do vértice inferior ao superior
        lowtriangle = self.drawline(lowtriangle[2][0], hightriangle[2][1], hightriangle[0][0], hightriangle[0][1], screen, False)

        print(hightriangle)
        print(lowtriangle)