#Proyecto discreta
#Julio marcos monzón
#Andrés Say Agosto
#Ayleen Rubio
from itertools import combinations


def repetidos(conjunto):
    lista = []
    sinRepetidos = ""
    for i in conjunto:
        lista.append(i)
    final = set(lista)
    final = sorted(final)
    for j in final:
        sinRepetidos += j
    return sinRepetidos
        
def elementos(sinrepetidos):
    listaFinal = []
    for i in sinrepetidos:
        listaFinal.append(i)
    return listaFinal

def potencia(c):
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s+[c[-1]] for s in r]

def imprime_ordenado(c):
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)
        
imprime_ordenado(potencia(["cereza", "chocolate", "fresa", "cereza"]))

print()

def combinaciones(c,n):
    return [s for s in potencia (c) if len(s) ==n]

imprime_ordenado(combinaciones(["cereza", "chocolate", "fresa", "cereza"],2))


#-------------------------------------------------------------------------
#Permutaciones
def permutacionesTotales(lista):
    if len(lista) == 0:
        return []
    elif len(lista) == 1:
        return [lista]
    else:
        temp = []
        for i in range(len(lista)):
            posicion = lista[i]
            px = lista[:i] + lista[i+1:]
            for j in permutacionesTotales(px):
                temp.append([posicion]+j)
        return temp

data =list("abc")
print("perm1")
for p in permutacionesTotales(data):
    print(p)

