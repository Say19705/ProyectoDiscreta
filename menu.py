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
flag = True
while flag:
    try:
        Kseleccion = int(input("Cuantos elementos desea seleccionar del conjunto: "))
        flag = False            
    except:
        print("Debes ingresar un número entero, menor o igual a la cantidad de elementos del conjunto, intente otra vez por favor :) \n")

flag = True
while flag:
    try:
        opcion = input("Ingrese lo que desea imprimir: \n1. permutaciones \n2. combinaciones \n3. ambas \n4. salir\n->")
        if opcion == "1":
            permFlag = True
        elif opcion == "2":
            listaF = pr.elementos(conjuntoCo)
            resultComb = pr.combinaciones(listaF, Kseleccion)
            imprimeComb=pr.imprime_ordenado(resultComb)
            combFlag = True
        elif opcion == "3":
            permFlag = True
            combFlag == True
        elif opcion == "4":
            print("Gracias por usar el programa")
            flag = False
    except:
        print("Has ingresado algo mal, intenta otra vez \n")
    
#-----------En teoría aqui van las impresiones
