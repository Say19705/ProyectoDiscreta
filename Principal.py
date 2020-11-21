#Proyecto discreta
#Julio marcos monzón
#Andrés Say Agosto
#Ayleen Rubio
from itertools import combinations

#colores=["rojo","azul","amarillo","Verde"]

#combinacion = list(combinations(colores,3))

#print(combinacion)
prueba = "hola"
listPrueba = []
llena = ""
for i in prueba:
    listPrueba.append(i)
final = set(listPrueba)
final = sorted(final)
print(final)
for j in final:
    llena += j
print(llena)
eliminados = len(prueba) - len(llena)
print(eliminados)

    





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

