lista = [10,20,30,40,50,60]
lista2 = [[3,4,5],[6,7,8],[9,10,11],[3,4,5],[6,7,8],[9,10,11]]

for x in lista:
    atuallist  = lista[lista.index(x)]
    atualindex = lista.index(x)
    
    if atualindex != len(lista)-1:
        nextlist   = lista[lista.index(x)+1]
        nextindex  = lista.index(x)+1
    
        print(f"lista atual = {x} | lista proximo = {nextlist}")
        print(f"indice atual = {atualindex} | indice proximo = {nextindex}")
        print(f"valor atual = {lista2[atualindex]} | valor proximo = {lista2[nextindex]}")
        print()
    else: 
        print(f"lista atual = {x} | lista proximo = {lista[0]}")
        print(f"indice atual = {atualindex} | indice proximo = {0}")
        print(f"valor atual = {lista2[atualindex]} | valor proximo = {lista2[0]}")
        print()
        