class mailmanager:
    def __init__(self, object3d) -> None:
        self.object3d = object3d
        self.zbuffer  = None
        
    def drawpixel(self, x, y, screen):
        screen.set_at((x, y), (255, 255, 255))
        
    def createzbuffer(self, window_size):
        zbuffer = [[0 for _ in range(window_size[0])] for _ in range(window_size[1])]
        self.zbuffer = zbuffer
        
    def checkzbuffer(self, y, x, z):
        buffervalue = self.zbuffer[y-1][x-1]
        if buffervalue == 0: return True    # Se a posição do buffer ainda não tiver sido escrito, escreva
        elif buffervalue > z: return True   # Se o z vigente for menor que o do buffer, escreva
        return False
    
    def scanline(self, vertices, screen):
        vertices.sort(key=lambda y: y[1])
        
        high   = vertices[0]
        medium = vertices[1]
        low    = vertices[2]
        
        fulltriangle  = self.drawline(high[0], high[1], high[2], low[0], low[1], low[2], screen, False)
        
        for y, point in enumerate(fulltriangle):
            if point[1] == medium[1]: 
                hightriangle = [high, point, medium]
                lowtriangle  = [medium, point, low]
                break

        hxa, hxb, hxc = hightriangle[0][0], hightriangle[1][0], hightriangle[2][0]
        hya, hyb, hyc = hightriangle[0][1], hightriangle[1][1], hightriangle[2][1]
        hza, hzb, hzc = hightriangle[0][2], hightriangle[1][2], hightriangle[2][2]

        lxc = lowtriangle[2][0]
        lyc = lowtriangle[2][1]
        lzc = lowtriangle[2][2]

        rightvertice, leftvertice = ([hxb,hyb,hzb], [hxc,hyc,hzc]) if hxb > hxc else ([hxc,hyc,hzc], [hxb,hyb,hzb])
        
        hrightline = self.drawline(hxa, hya, hza, rightvertice[0], rightvertice[1], rightvertice[2], screen, True)
        hleftline  = self.drawline(hxa, hya, hza, leftvertice[0], leftvertice[1], leftvertice[2], screen, True)
                
        lrightline = self.drawline(lxc, lyc, lzc, rightvertice[0], rightvertice[1], rightvertice[2], screen, True)
        lleftline  = self.drawline(lxc, lyc, lzc, leftvertice[0], leftvertice[1], leftvertice[2], screen, True)
        
        ilen = len(hleftline)
        for i in range(ilen):
            self.drawline(hrightline[i][0], hrightline[i][1], hrightline[i][2], hleftline[i][0], hleftline[i][1], hleftline[i][2] , screen)
            
            
        ilen = len(lrightline)
        for i in range(ilen):
            self.drawline(lrightline[i][0], lrightline[i][1], lrightline[i][2], lleftline[i][0], lleftline[i][1], lleftline[i][2], screen)              

    def drawline(self, x0, y0, z0, x1, y1, z1, screen, draw=True):
        max_diff = max(abs(x1 - x0), abs(y1 - y0), abs(z1 - z0))
        num_points = int(max_diff)  # Determina o número de pontos automaticamente

        interpolated_points = []

        for i in range(num_points + 1):
            if num_points == 0: t=0
            else: t = i / num_points  # Fator de interpolação entre 0 e 1
            x = round(x0 + t * (x1 - x0))
            y = round(y0 + t * (y1 - y0))
            z = round(z0 + t * (z1 - z0))
            dupindex = [sublista[1] for sublista in interpolated_points]
            if dupindex.count(y) == 0:  
                interpolated_points.append([x, y, z])
            
            if self.checkzbuffer(y, x, z):
                if draw == True: 
                    screen.set_at((x, y), (255, 255, 255))
                    self.zbuffer[y-1][x-1] = z     
                    
        return interpolated_points

        

