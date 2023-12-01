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

        while True:
            deltaerror = 2 * error
           
            dupindex = [sublista[1] for sublista in list]
            if dupindex.count(y) == 0:
                list.append([x, y])
                
            if x == x1 and y == y1: break
           
            if deltaerror > -deltay:
                error -= deltay
                if x0 < x1: x += 1
                else: x -= 1

            if deltaerror < deltax:
                error += deltax
                if y0 < y1: y += 1
                else: y -= 1
           
            if draw == True: 
                screen.set_at((x, y), (255, 255, 255))
            
            if draw and (x != x0 or y != y0):  # Adicione o ponto inicial se ele não estiver no final
                screen.set_at((x0, y0), (255, 255, 255))
            
        return list
            
    def scanline(self, vertices, screen):
        vertices.sort(key=lambda y: y[1])
        
        high   = vertices[0]
        medium = vertices[1]
        low    = vertices[2]
        
        fulltriangle  = self.drawline(high[0], high[1], low[0], low[1], screen, False)
        
        for y, point in enumerate(fulltriangle):
            if point[1] == medium[1]: 
                hightriangle = [high, point, medium]
                lowtriangle  = [medium, point, low]
                break

        hxa, hxb, hxc = hightriangle[0][0], hightriangle[1][0], hightriangle[2][0]
        hya, hyb, hyc = hightriangle[0][1], hightriangle[1][1], hightriangle[2][1]

        lxc = lowtriangle[2][0]
        lyc = lowtriangle[2][1]

        rightvertice, leftvertice = ([hxb,hyb], [hxc,hyc]) if hxb > hxc else ([hxc,hyc], [hxb,hyb])
        
        hrightline = self.drawline(hxa, hya, rightvertice[0], rightvertice[1], screen, False)
        hleftline  = self.drawline(hxa, hya, leftvertice[0], leftvertice[1], screen, False)
                
        lrightline = self.drawline(lxc, lyc, rightvertice[0], rightvertice[1], screen, False)
        lleftline  = self.drawline(lxc, lyc, leftvertice[0], leftvertice[1], screen, False)
        
        ilen = len(hleftline)
        for i in range(ilen): self.drawline(hrightline[i][0], hrightline[i][1], hleftline[i][0], hleftline[i][1], screen)
            
        ilen = len(lrightline)    
        for i in range(ilen): self.drawline(lrightline[i][0], lrightline[i][1], lleftline[i][0], lleftline[i][1], screen)