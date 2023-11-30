lista_de_listas = [
    [3, 7, 1],
    [9, 4, 5],
    [6, 2, 8]
]

indice_para_ordenar = 0  # Índice que você deseja usar para ordenar as sublistas

lista_de_listas.sort(key=lambda x: x[indice_para_ordenar])

print(lista_de_listas)