# Ejercicio 4: Calcula el pago segun el rango de horas de permanencia
#Variables
hora = 0 #int
minutos = 0 #int
pago = 0.0 #float
#Codigo
hora = int(input("Ingrese la hora de entrada del vehiculo: "))
minutos = int(input("Ingrese los minutos de entrada del vehiculo: "))
if minutos > 0:
    hora = hora + 1
    minutos = 0
if hora < 2:
    pago = hora * 20
elif hora >= 2 and hora <= 5:
    pago = hora * 18
elif hora > 5:
    pago = hora * 15
print("El pago por el tiempo de estacionamiento es de: $", pago)
#:D
