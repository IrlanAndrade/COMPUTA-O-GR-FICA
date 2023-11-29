# Função para rasterizar linhas entre pontos
def draw_lines_between_points(points):
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        
        # Algoritmo de Bresenham para rasterização de linhas
        deltax, deltay = x1 - x0, y1 - y0
        dydx2 = 2 * deltay
        dydx2_minus_dx2 = dydx2 - 2 * deltax
        error = dydx2 - deltax
        
        y = y0
        for x in range(x0, x1 + 1):
            # Conectar o último ponto à coordenada final
            if x == x1:
                y = y1 if y1 > y0 else y0
            print(x, y)  # Aqui, você pode processar ou desenhar os pontos
            
            if error >= 0:
                y += 1
                error += dydx2_minus_dx2
            else:
                error += dydx2

# Lista de pontos (coordenadas x, y)
points = [(1, 1), (8, 5), (4, 9), (2, 7), (10, 12)]

# Chama a função para rasterizar linhas entre os pontos
draw_lines_between_points(points)