# Ejercicio 11: Busca una matricula en el historial de vehiculos
#Variables
matricula = "" #string
tipov = 0 #int
horas = 0 #int
minutos = 0 #int
flag = 1 #int
vehit = 0 #int
carros = 0 #int
motos = 0 #int
camionetas = 0 #int
camiones = 0 #int
recaudacion = 0.0 #float
pago = 0.0 #float
fl = 1 #int
listplacas = [] #list
encontrada = 0 #int
posicion = 0 #int
i = 0 #int
buscada = "" #string
#Codigo
while flag == 1:
    matricula = (input("Ingrese la matricula del vehiculo: "))
    tipov = int(input("Ingrese el tipo de vehiculo \n1. Motocicleta $10 \n2. Automovil $15 \n3. Camioneta $20 \n4. Autobus $30 \n"))
    horas = int(input("Ingrese las horas de permanencia del vehiculo: "))
    minutos = int(input("Ingrese los minutos de permanencia del vehiculo: "))
    if minutos > 0:
        horas = horas + 1

    pago = 0.0
    fl = 1
    match tipov:
        case 1:
            pago = horas * 10
            motos = motos + 1
            vehit = vehit + 1
            recaudacion = recaudacion + pago
        case 2:
            pago = horas * 15
            carros = carros + 1
            vehit = vehit + 1
            recaudacion = recaudacion + pago
        case 3:
            pago = horas * 20
            camionetas = camionetas + 1
            vehit = vehit + 1
            recaudacion = recaudacion + pago
        case 4:
            pago = horas * 30
            camiones = camiones + 1
            vehit = vehit + 1
            recaudacion = recaudacion + pago
        case _:
            print("Tipo de vehiculo no valido")
            fl = 0

    if fl == 1:
        print("Las horas de permanencia son: ", horas)
        print("El pago por el tiempo de estacionamiento es de: $", pago)
        print("Los espacios que quedan disponibles son: ", 30 - vehit)
        listplacas.append(matricula)
        buscada = matricula
        for i in range(len(listplacas)):
            if listplacas[i] == matricula and encontrada == 0:
                encontrada = 1
                posicion = i + 1
            if encontrada == 1:
                print("La matricula", matricula, "se encuentra en el historial, en la posicion", posicion)
            else:
                print("La matricula", matricula, "no se encuentra en el historial")

    if vehit == 30:
        print("El estacionamiento esta lleno")
        flag = 0
    else:
        flag = int(input("Desea ingresar otro vehiculo? \n1. Si \n2. No \n"))

print("El total de vehiculos que ingresaron fueron: ", vehit)
print("El total de motocicletas que ingresaron fueron: ", motos)
print("El total de automoviles que ingresaron fueron: ", carros)
print("El total de camionetas que ingresaron fueron: ", camionetas)
print("El total de autobuses que ingresaron fueron: ", camiones)
print("La recaudacion total fue de: $", recaudacion)

print("Las matriculas de los vehiculos que ingresaron son: ")
for matricula in listplacas:
    print("La matricula del vehiculo es: ", matricula)
#:D
