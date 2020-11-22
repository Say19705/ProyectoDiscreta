#Proyecto discreta
#Julio marcos monzón
#Andrés Say Agosto
#Ayleen Rubio

import Principal as pr

#1
print("------------------------------------------------")
print("-------------Menasaje de Bienvenida-------------")
conjunto = input("Ingrese un conjunto de letras: ")
conjuntoCo = pr.repetidos(conjunto)
print(conjuntoCo)
conjuntoPe = conjunto
combFlag = False
permFlag = False
Kseleccion = input("Cuantos elementos desea seleccionar del conjunto: ")
opcion = input("Ingrese lo que desea imprimir: \n1. permutaciones \n2. combinaciones \n3. ambas \n->")
if opcion == "1":
    permFlag = True
elif opcion == "2":
    combFlag = True
elif opcion == 3:
    permFlag = True
    combFlag == True
    
#-----------En teoría aqui van las impresiones
