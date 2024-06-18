#By Lucy Nest

#Objetivo
#Una aplicacion que registre pedidos de gas antes de ser enviados

#------------------------------------------------------------------------
#Definiciones

import funciones as fun
#this is where the "fun" begins

#Definir al menos 3 sectores como parte de alguna coleccion
sectores = ["Centro", "Colina", "Industrias"]

entrada = 0

pedidos = []

repetir = True

#------------------------------------------------------------------------
#Menú

#While
while entrada != 4:

    #Mostrar menú con 4 opciones; Registrar pedido, listar los pedidos, imprimir hoja de ruta, y salir del programa.
    print("""
    1) Registrar pedido
    2) Listar los pedidos
    3) Imprimir hoja de ruta
    4) Salir del programa
    """)

    #Pedir entrada
    try:
        entrada = int(input(">"))
    except:
        print("Ingrese un numero válido")
        entrada = 0
    if (entrada != 0) and (entrada != 1) and (entrada != 2) and (entrada != 3) and (entrada != 4):
        print("Ingrese un numero válido")

    #------------------------------------------------------------------------
    #Procesos

    #Registrar pedido
    if entrada == 1:
        #Pedir nombre y apellido
        nom = input("Nombre: ")

        #Pedir dirección
        dir = input("Direccion: ")

        #Pedir detalle
        print("Seleccione la cantidad de cilindros a pedir")
        while repetir == True:
            try:
                cil5 = int(input("Cilindros de 5kg: "))
            except:
                print("Ingrese un numero valido")
                cil5 = -1
            if cil5 >= 0:
                repetir = False
        repetir = True
        while repetir == True:
            try:
                cil15 = int(input("Cilindros de 15kg: "))
            except:
                print("Ingrese un numero valido")
                cil15 = -1
            if cil15 >= 0:
                repetir = False
        repetir = True
        while repetir == True:
            try:
                cil45 = int(input("Cilindros de 5kg: "))
            except:
                print("Ingrese un numero valido")
                cil45 = -1
            if cil45 >= 0:
                repetir = False
        repetir = True
        det = [cil45, cil15, cil45]

        #Validar los datos

        #Llamar a la funcion
        pedidos = fun.registrar(nom, dir, det, pedidos)

    #Listar los pedidos
    elif entrada == 2:
        fun.listar(pedidos)

    #Imprimir hoja de ruta
    elif entrada == 3:
        while repetir == True: 
            sec = input("Seleccione un sector: ")
            if (sec not in sectores) and (sec != "x"):
                print("Seleccione un sector válido o ingrese x para salir")
            else:
                repetir = False
        repetir = True

        fun.imprimir(sec, pedidos)

    #------------------------------------------------------------------------
    #Salidas

#Salir del programa
print()
print("Muchas gracias por usar el programa")