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
#Codigo
while flag == 1:
    matricula = (input("Ingrese la matricula del vehiculo: "))
    tipov = int(input("Ingrese el tipo de vehiculo \n1. Motocicleta $10 \n2. Automovil $15 \n3. Camioneta $20 \n4. Autobus $30 \n"))
    horas = int(input("Ingrese las horas de permanencia del vehiculo: "))
    minutos = int(input("Ingrese los minutos de permanencia del vehiculo: "))
    if minutos > 0:
        horas = horas + 1
        minutos = 0
    match tipov:
        case 1:
            pago = horas * 10
            motos = motos + 1
            recaudacion = recaudacion + pago
        case 2:
            pago = horas * 15
            carros = carros + 1
            recaudacion = recaudacion + pago
        case 3:
            pago = horas * 20
            camionetas = camionetas + 1
            recaudacion = recaudacion + pago
        case 4:
            pago = horas * 30
            camiones = camiones + 1
            recaudacion = recaudacion + pago
        case _:
            print("Tipo de vehiculo no valido")
    print("Las horas de permanencia son: ", horas)
    print("El pago por el tiempo de estacionamiento es de: $", pago)
    flag = int(input("Desea ingresar otro vehiculo? \n1. Si \n2. No \n"))
vehit = motos + carros + camionetas + camiones
print("El total de vehiculos que ingresaron fueron: ", vehit)
print("El total de motocicletas que ingresaron fueron: ", motos)
print("El total de automoviles que ingresaron fueron: ", carros)
print("El total de camionetas que ingresaron fueron: ", camionetas)
print("El total de autobuses que ingresaron fueron: ", camiones)
print("La recaudacion total fue de: $", recaudacion)
#:D
