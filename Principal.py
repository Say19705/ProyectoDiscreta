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

    



