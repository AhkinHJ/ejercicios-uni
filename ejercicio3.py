#Variables 
horas = 0 #int
minutos = 0 #int
pago = 0.0 #float
#Codigo
horas = int(input("Ingrese las horas de permanencia del vehiculo: "))
minutos = int(input("Ingrese los minutos de permanencia del vehiculo: "))
if minutos > 0:
    horas = horas + 1
    minutos = 0
pago = horas * 15
print("Las horas de permanencia son: ", horas)
print("El pago por el tiempo de estacionamiento es de: $", pago)
#:D