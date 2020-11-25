#Proyecto Final
#Matematica Discreta 1 seccion 10
#Julio Marcos Monzón 19226
#Andrés Say Agosto 19705
#Ayleen Rubio 19003

#Referencias consultadas:
#http://edupython.blogspot.com/2016/06/combinaciones-permutaciones-y-otras.html
#http://edupython.blogspot.com/2016/06/potenciando-conjuntos.html
#

from itertools import combinations


def repetidos(conjunto):
    lista = [] #Iniciar una lista vacia
    sinRepetidos = ""
    for i in conjunto:
        lista.append(i) #Agregar cada uno de los elementos del conjunto ingresado
    final = set(lista) #Eliminar valores repetidos
    final = sorted(final) #Ordenarlos
    for j in final: #Concatenar los elementos
        sinRepetidos += j
    return sinRepetidos #Devolver conjunto sin elementos repetidos
        
def elementos(conjunto): #Hacer una lista con los elementos del conjunto separados
    listaFinal = []
    for i in conjunto:
        listaFinal.append(i)
    return listaFinal

def ConjuntoPotencia(cnjnto):
    if len(cnjnto) == 0: #Si el conjunto es vacio, el conjunto potencia es vacio
        return [[]]
    r = ConjuntoPotencia(cnjnto[:-1]) #Almacenar lo obtenido en la recursividad
    r = r+ [s+[cnjnto[-1]] for s in r] #Procesar subconjuntos s que se encuentran en r y agregar ultimo elemento
    return r #Todo r concatenado

def MostrarOrdenado(cnjnto):
    for e in sorted(cnjnto, key=lambda s: (len(s), s)): #Ordenar comparando longitud y elementos
        print(e)
        
print()

def combinaciones(cnjnto,n): #Obtener únicamente los subconjuntos con n elementos
    devolver = [s for s in ConjuntoPotencia (cnjnto) if len(s) == n]
    return devolver

#-------------------------------------------------------------------------
#Permutaciones
def insertar(x, oldList, i): #Insertar x dentro de la lista enterior en posicion i
    newList = oldList[:i]+[x]+oldList[i:] #Todo se devuelve concatenado
    return newList
def posiblesInsertar(x, oldList): #Mostrar todos los posibles casos donde se puede ingresar el valor
    newList = [insertar(x,oldList,i) for i in range(len(oldList)+1)]
    return newList

def permutacion(conjunto): #Generar todas las permutaciones recursivamente
    if len(conjunto) == 0:
        return [[]]
    perFinal = sum([posiblesInsertar(conjunto[0],s) for s in permutacion(conjunto[1:])],[]) #Sum para concatenar las listas generadas
    return perFinal

def permutarConK (cnjnto, n): #Calcular y mostrar permutaciones con k elementos
    devolver = sum([permutacion(s)
                    for s in combinaciones(cnjnto,n)],
                   [])
    return devolver
