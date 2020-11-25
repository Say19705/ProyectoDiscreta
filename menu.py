#Proyecto discreta
#Julio marcos monzón
#Andrés Say Agosto
#Ayleen Rubio

#Importar el módulo de funciones 
import Principal as pr


#Comenzar el programa con un mensaje de bienvenida
print("-------------Menasaje de Bienvenida-------------")
#Pedir el conjunto de valores
conjunto = input("Ingrese un conjunto de letras: ")
#Como en combinaciones es necesario eliminar los elementos repetidos porque el orden no importa, se crea un conjunto si elementos
conjuntoCo = pr.repetidos(conjunto)
#Se crea un conjunto para permutaciones
conjuntoPe = conjunto

#combFlag = False
#permFlag = False

#Bandera para el ciclo while de elegir el valor k
flag = True
#Inicio del ciclo while
while flag:
    #Try por si el usuario ingresa algo equivocado
    try:
        #ingreso del valor k
        Kseleccion = int(input("Cuantos elementos desea seleccionar del conjunto: "))
        #verifica que la k no sea mayor a la cantidad de elementos del conjunto, si lo es, vuelve a pedir el valor k
        if Kseleccion > len(conjunto):
            print(len(conjunto))
            print("Debes ingresar un valor menor o igual a la cantidad de elementos del conjunto")
            flag = True
        else:
            #Se sale del ciclo
            flag = False
    except:
        print("Has ingresado algo incorrecto, intenta otra vez \n")

#nueva bandera para el ciclo while del menu
flag = True
#Inicio del ciclo while
while flag:
    #Try para agarrar errores de ingreso
    try:
        #Ingreso de las opciones del usuario
        opcion = input("Ingrese lo que desea imprimir: \n1. permutaciones \n2. combinaciones \n3. ambas \n4. salir\n->")
        #popcion 1 permutaciones
        if opcion == "1":
            print("--------------------Permutaciones----------------------")
            permFlag = True
        #opcion 2 combinaciones
        elif opcion == "2":
            #bandera para ciclo while de verificacion
            bandera2 = True
            #igualar la k ingresada
            newk = Kseleccion
            #Inicio del while, debido a que se ha disminuido el valor de elementos elimando los repetidos, se verifica que sea menor o igual a la cantidad de elementos 
            while bandera2:
                if Kseleccion > len(conjuntoCo):
                    #mostrar conjunto sin repetir
                    print("Este es el conjunto sin elementos repetidos: ",conjuntoCo)
                    newK = int(input("Su valor k es menor a la cantidad de valores sin repetir, para mostrar las combinaciones, elija de nuevo: \n"))
                    #verificar que sea menor
                    if newk > len(conjuntoCo):
                        print("Ha vuelto a ingresar un valor erróneo")
                    else:
                        bandera2 = False
                else:
                    bandera2 = False
            #Convetir el conjunto de conbinaciones en lista 
            listaF = pr.elementos(conjuntoCo)
            #Obtener la lista de combinaciones posibles para el valor k
            resultComb = pr.combinaciones(listaF, newk)
            #Impirmir resultado
            imprimeComb=pr.imprime_ordenado(resultComb)
        #opcion 3 permutaciones y combinaciones
        elif opcion == "3":
            #bandera para ciclo while de verificacion
            bandera2 = True
            #igualar la k ingresada
            newk = Kseleccion
            #Inicio del while, debido a que se ha disminuido el valor de elementos elimando los repetidos, se verifica que sea menor o igual a la cantidad de elementos 
            while bandera2:
                if Kseleccion > len(conjuntoCo):
                    #mostrar conjunto sin repetir
                    print("Este es el conjunto sin elementos repetidos: ",conjuntoCo)
                    newK = int(input("Su valor k es menor a la cantidad de valores sin repetir, para mostrar las combinaciones, elija de nuevo: \n"))
                    #verificar que sea menor
                    if newk > len(conjuntoCo):
                        print("Ha vuelto a ingresar un valor erróneo")
                    else:
                        bandera2 = False
                else:
                    bandera2 = False
            print("---------------Combinaciones----------------")
            #Convetir el conjunto de conbinaciones en lista 
            listaF = pr.elementos(conjuntoCo)
            #Obtener la lista de combinaciones posibles para el valor k
            resultComb = pr.combinaciones(listaF, newk)
            #Impirmir resultado
            imprimeComb=pr.imprime_ordenado(resultComb)
            print("----------------Combinaciones--------------")
        #Opcion 4 salir del menu
        elif opcion == "4":
            print("Gracias por usar el programa")
            flag = False
    except:
        print("Has ingresado algo mal, intenta otra vez \n")
    
#-----------En teoría aqui van las impresiones
