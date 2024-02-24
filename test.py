lista = [[1,2],[1,2]]
set_de_frozensets = {frozenset(l) for l in lista}
set_de_frozensets = set(set_de_frozensets)
lista = [list(frozenset) for frozenset in set_de_frozensets]
print(lista)