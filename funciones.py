#Registrar pedido
def registrar(nombre, direccion, detalle, pedidos):
    orden = [nombre, direccion, detalle]

    pedidos.append(orden)

    return(pedidos)

#Listar los pedidos
def listar(pedidos):
    #Mostrar una tabla con todos los pedidos
    for orden in pedidos:
        for item in orden:
            print(item)
        print()

#Imprimir hoja de ruta
def imprimir(sector, pedidos):
    nombreArchivo = sector + ".txt"
    archivo = open(nombreArchivo, "w")

    #Pedir uno de los sectores válidos
    for orden in pedidos:
        if orden[1] == sector:
            aimprimir = orden[0] + "       Cilindros5:" + orden[2][0] + "       Cilindros15:" + orden[2][1] + "       Cilindros45" + orden[2][2] + "\n"
            archivo.write(aimprimir)

    archivo.close()