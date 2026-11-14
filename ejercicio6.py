#Variables
tipc = 0 #int
horas = 0 #int
minutos = 0 #int
pago = 0.0 #float
#Codigo
horas = int(input("Ingrese las horas de permanencia del vehiculo: "))
minutos = int(input("Ingrese los minutos de permanencia del vehiculo: "))
if minutos > 0:
    horas = horas + 1
    minutos = 0
tipc = int(input("Ingrese el tipo de vehiculo \n1. Motocicleta $10 \n2. Automovil $15 \n3. Camioneta $20 \n4. Autobus $30 \n"))
if tipc == 1:
    pago = horas * 10
elif tipc == 2:
    pago = horas * 15
elif tipc == 3:
    pago = horas * 20
elif tipc == 4:
    pago = horas * 30
else:
    print("Tipo de vehiculo no valido")
print("Las horas de permanencia son: ", horas)
print("El pago por el tiempo de estacionamiento es de: $", pago)
#:D