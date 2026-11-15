# Ejercicio 18: Tabla de registro y salida con calculo del importe
#Variables
tabla = [
    [1, "LIBRE", "LIBRE", 0, 0, 0, 0],
    [2, "LIBRE", "LIBRE", 0, 0, 0, 0],
    [3, "LIBRE", "LIBRE", 0, 0, 0, 0]
] #Matriz
fila = 3 #int
columna = 7 #int
placa = "" #string
placabus = "" #string
tipov = 0 #int
horaent = 0 #int
horasal = 0 #int
minutos = 0 #int
permanencia = 0 #int
importe = 0.0 #float
tarifa = 0 #int
op = 1 #int
encontrado = 0 #int
i = 0 #int
j = 0 #int
#Codigo
while op != 0:
    op = int(input("\nIngrese una opcion:\n1. Ver tabla del estacionamiento\n2. Registrar un vehiculo\n3. Salida de un vehiculo\n0. Salir.\n"))
    match op:
        case 1:
            print("\nTabla del estacionamiento:")
            print("Espacio Placa Tipo Entrada Salida Permanencia Importe")
            for i in range(fila):
                for j in range(columna):
                    print(tabla[i][j], end=" ")
                print()
        case 2:
            encontrado = 0
            for i in range(fila):
                if tabla[i][1] == "LIBRE" and encontrado == 0:
                    encontrado = 1
                    placa = input("Placa del vehiculo: ")
                    tipov = int(input("Ingrese el tipo de vehiculo \n1. Motocicleta $10 \n2. Automovil $15 \n3. Camioneta $20 \n4. Autobus $30 \n"))
                    match tipov:
                        case 1:
                            tabla[i][2] = "Motocicleta"
                        case 2:
                            tabla[i][2] = "Automovil"
                        case 3:
                            tabla[i][2] = "Camioneta"
                        case 4:
                            tabla[i][2] = "Autobus"
                    horaent = int(input("Hora de entrada: "))
                    tabla[i][1] = placa
                    tabla[i][3] = horaent
                    print("Vehiculo registrado en el espacio ", tabla[i][0], ".")
            if encontrado == 0:
                print("No hay espacios libres.")
        case 3:
            placabus = input("\nIngrese la placa del vehiculo que va a salir: ")
            encontrado = 0
            for i in range(fila):
                if tabla[i][1] == placabus and encontrado == 0:
                    encontrado = 1
                    horasal = int(input("Hora de salida: "))
                    minutos = int(input("Minutos de salida: "))
                    permanencia = horasal - tabla[i][3]
                    if minutos > 0:
                        permanencia = permanencia + 1
                    if permanencia < 1:
                        permanencia = 1
                    match tabla[i][2]:
                        case "Motocicleta":
                            tarifa = 10
                        case "Automovil":
                            tarifa = 15
                        case "Camioneta":
                            tarifa = 20
                        case "Autobus":
                            tarifa = 30
                    importe = permanencia * tarifa
                    tabla[i][4] = horasal
                    tabla[i][5] = permanencia
                    tabla[i][6] = importe
                    print("La placa ", placabus, " de tipo ", tabla[i][2], " permanecio ", tabla[i][5], " hora(s). Importe a pagar: $", tabla[i][6])
                    tabla[i][1] = "LIBRE"
                    tabla[i][2] = "LIBRE"
                    tabla[i][3] = 0
                    tabla[i][4] = 0
                    tabla[i][5] = 0
                    tabla[i][6] = 0
                    print("Espacio liberado.")
            if encontrado == 0:
                print("La placa no se encuentra en el estacionamiento.")
        case 0:
            print("Saliendo...")
        case _:
            print("Opcion no valida.")
#:D
