# Ejercicio 12: Menu para registrar y sacar vehiculos (15 espacios)
#Variables
lisvehi = [] #list
vehiculos = 0 #int
matricula = "" #string
flg = 1 #int
op = 0 #int
i = 0 #int
#Codigo
while flg == 1:
    print("Bienvenido al estacionamiento")
    print("1. Registrar un vehiculo")
    print("2. Salir del estacionamiento")
    print("3. Consultar placas de vehiculos")
    print("4. Vehiculos en el estacionamiento")
    print("5. Espacios disponibles")
    print("0. Salir del programa")
    op = int(input("Ingrese una opcion: "))
    match op:
        case 1:
            if vehiculos >= 15:
                print("No se pueden ingresar mas vehiculos")
            else:
                matricula = input("Ingrese la matricula del vehiculo: ")
                lisvehi.append(matricula)
                vehiculos += 1
                print("Vehiculo registrado con exito")
        case 2:
            if vehiculos == 0:
                print("No hay vehiculos en el estacionamiento")
            else:
                matricula = input("Ingrese la matricula del vehiculo a salir: ")
                for i in range(len(lisvehi)):
                    if lisvehi[i] == matricula:
                        lisvehi.pop(i)
                        vehiculos -= 1
                        print("Vehiculo retirado con exito")
        case 3:
            if vehiculos == 0:
                print("No hay vehiculos en el estacionamiento")
            else:
                print("Placas de los vehiculos en el estacionamiento:")
                for i in range(len(lisvehi)):
                    print(lisvehi[i])
        case 4:
            print("Vehiculos en el estacionamiento:", vehiculos)
        case 5:
            print("Espacios disponibles:", 15 - vehiculos)
        case 0:
            flg = 0
            print("Gracias por usar el estacionamiento")
        case _:
            print("Opcion no valida")
#:D
