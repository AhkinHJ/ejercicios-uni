#Variables
#Ejemplo de matriz
espaesta = [
    ["ABC123","LIBRE","XYZ456"],
    ["LIBRE","DEF789","LIBRE"],
    ["GHI321","LIBRE","LIBRE"]
] #Matriz
fila = 3 #int
espacio = 3 #int
fibus = 0 #int
espaciobus = 0 #int
placa = "" #string
placabus = "" #string
op = 1 #int
encontrado = 0 #int
#Codigo
while op != 0:
    op = int(input("\nIngrese una opcion:\n1. Ver distribucion del estacionamiento\n2. Registrar un vehiculo\n3. Consultar ubicacion de una placa\n0. Salir.\n"))
    match op:
        case 1:
            print("\nDistribucion del estacionamiento:")
            for i in range(fila):
                for j in range(espacio):
                    print(espaesta[i][j], end=" ")
                print()
        case 2:
            fibus = int(input("\nFila en la que se va a registrar: "))
            espaciobus = int(input("Espacio en el que se va a registrar: "))
            placa = input("Placa del vehiculo: ")
            fibus = fibus - 1
            espaciobus = espaciobus - 1
            espaesta[fibus][espaciobus] = placa
            print("Vehiculo registrado.")
        case 3:
            placabus = input("\nIngrese la placa a consultar: ")
            encontrado = 0
            for i in range(fila):
                for j in range(espacio):
                    if espaesta[i][j] == placabus:
                        print("La placa ", placabus, " se encuentra en la fila ", i + 1, " espacio ", j + 1)
                        encontrado = 1
            if encontrado == 0:
                print("La placa no se encuentra en el estacionamiento.")
        case 0:
            print("Saliendo...")
        case _:
            print("Opcion no valida.")