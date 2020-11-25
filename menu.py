#Proyecto Final
#Matematica Discreta 1 seccion 10
#Julio Marcos Monzón 19226
#Andrés Say Agosto 19705
#Ayleen Rubio 19003

#Importar el módulo de funciones 
import modulo as pr


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
flag1 = True
#Inicio del ciclo while
while flag1:
    #Try por si el usuario ingresa algo equivocado
    try:
        #ingreso del valor k
        Kseleccion = int(input("Cuantos elementos desea seleccionar del conjunto: "))
        #verifica que la k no sea mayor a la cantidad de elementos del conjunto, si lo es, vuelve a pedir el valor k
        if Kseleccion == -1:
            print("A continuacion se le mostrarán todas las posibles opciones tanto de combinaciones como de permutaciones\n")
            print("--------------------Combinaciones----------------------")
            listaF = pr.elementos(conjuntoCo) #Convetir el conjunto de combinaciones en lista
            potenciaC = pr.ConjuntoPotencia(listaF) #Obtener el conjunto potencia
            pr.MostrarOrdenado(potenciaC) #Mostrar el conjunto potencia
            print("--------------------Permutaciones----------------------")
            listaF = pr.elementos(conjuntoPe) #Convertir el conjunto de permutaciones en lista
            potenciaP = pr.permutacion(listaF) #Obtener todas las permutaciones posibles
            pr.MostrarOrdenado(potenciaP) #Mostrar todas las permutaciones posibles
            flag1 = False
            print("Gracias por utilizar el programa")
        elif Kseleccion > len(conjunto):
            print("Debes ingresar un valor menor o igual a la cantidad de elementos del conjunto, intentelo de nuevo por favor \n")
            flag1 = True
        else:
            #Se sale del ciclo
            flag1 = False
    except:
        print("Has ingresado algo incorrecto, intenta otra vez \n")

#nueva bandera para el ciclo while del menu
flag = True
if Kseleccion == -1:
    flag = False
#Inicio del ciclo while
while flag:
    #Try para agarrar errores de ingreso
    try:
        #Ingreso de las opciones del usuario
        opcion = input("Ingrese lo que desea imprimir: \n1. permutaciones \n2. combinaciones \n3. ambas \n4. salir\n->")
        #popcion 1 permutaciones
        if opcion == "1":
            print("--------------------Permutaciones----------------------")
            listaF = pr.elementos(conjuntoPe) #Convetir el conjunto de combinaciones en lista 
            resultPerm = pr.permutarConK(listaF,Kseleccion) #Obtener la lista de permutaciones posibles para el valor k
            imprimePerm = pr.MostrarOrdenado(resultPerm) #Impirmir resultado
            permFlag = True
        #opcion 2 combinaciones
        elif opcion == "2":
            print("--------------------Combinaciones----------------------")
            #bandera para ciclo while de verificacion
            bandera2 = True
            #igualar la k ingresada
            newk = Kseleccion
            #Inicio del while, debido a que se ha disminuido el valor de elementos elimando los repetidos, se verifica que sea menor o igual a la cantidad de elementos 
            while bandera2:
                if Kseleccion > len(conjuntoCo):
                    #mostrar conjunto sin repetir
                    print("Este es el conjunto sin elementos repetidos: ",conjuntoCo)
                    newk = int(input("Su valor k es mayor a la cantidad de valores sin repetir, para mostrar las combinaciones, elija de nuevo: "))
                    #verificar que sea menor
                    if newk > len(conjuntoCo):
                        print("Ha vuelto a ingresar un valor erróneo")
                    else:
                        bandera2 = False
                else:
                    bandera2 = False
            #Convetir el conjunto de combinaciones en lista 
            listaF = pr.elementos(conjuntoCo)
            #Obtener la lista de combinaciones posibles para el valor k
            resultComb = pr.combinaciones(listaF, newk)
            #Impirmir resultado
            imprimeComb=pr.MostrarOrdenado(resultComb)
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
                    newk = int(input("Su valor k es mayor a la cantidad de valores sin repetir, para mostrar las combinaciones, elija de nuevo: "))
                    #verificar que sea menor
                    if newk > len(conjuntoCo):
                        print("Ha vuelto a ingresar un valor erróneo")
                    else:
                        bandera2 = False
                else:
                    bandera2 = False
            print("---------------Combinaciones----------------")
            #Convetir el conjunto de combinaciones en lista 
            listaF = pr.elementos(conjuntoCo)
            #Obtener la lista de combinaciones posibles para el valor k
            resultComb = pr.combinaciones(listaF, newk)
            #Impirmir resultado
            imprimeComb=pr.MostrarOrdenado(resultComb)
            print("----------------Permutaciones--------------")
            listaF2 = pr.elementos(conjuntoPe) #Convetir el conjunto de combinaciones en lista 
            resultPerm = pr.permutarConK(listaF2,Kseleccion) #Obtener la lista de permutaciones posibles para el valor k
            pr.MostrarOrdenado(resultPerm) #Impirmir resultado
        #Opcion 4 salir del menu
        elif opcion == "4":
            print("Gracias por usar el programa")
            flag = False
    except:
        print("Has ingresado algo mal, intenta otra vez \n")
    