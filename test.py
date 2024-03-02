def remover_duplicatas(lista_de_listas):
    # Usar um conjunto para manter as tuplas únicas
    conjunto_unico = set()

    # Lista resultante sem duplicatas
    lista_sem_duplicatas = []

    for lista in lista_de_listas:
        # Convertendo a lista interna em uma tupla
        tupla_da_lista = tuple(lista)

        # Verificando se a tupla já está no conjunto
        if tupla_da_lista not in conjunto_unico:
            # Adicionando a tupla única à lista resultante
            lista_sem_duplicatas.append(lista)
            
            # Adicionando a tupla ao conjunto para evitar duplicatas
            conjunto_unico.add(tupla_da_lista)

    return lista_sem_duplicatas


newadjvertices  = [[[[360, 380, 887], [360, 380, 887], [360, 380, 887], [360, 380, 887], [360, 380, 887], [360, 380, 887], [395, 395, 890], [395, 395, 890], [395, 395, 890], [395, 395, 890], [395, 395, 890], [395, 395, 890], [396, 384, 883], [396, 384, 883], [396, 384, 883], [396, 384, 883], [396, 384, 883], [396, 384, 883]]]]
for adjvertices in newadjvertices:
        # #print(f"adjvertices {adjvertices}")
        
        for vertices in adjvertices:
            for v in vertices:
                print(f"vertices: {v}")
            vertices = remover_duplicatas(vertices)
            # vertices = {frozenset(l) for l in vertices}
            # vertices = set(vertices)
            # vertices = [list(frozenset) for frozenset in vertices]
            print(vertices)
            
            