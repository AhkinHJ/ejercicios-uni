# Ejercicio 2: Calcula el tiempo de estacionamiento en horas y minutos
#Variables
horaentrada = 0 #int
minutoentrada = 0 #int
horasalida = 0 #int
minutosalida = 0 #int
horas = 0 #int
minutos = 0 #int
#Codigo
horaentrada = int(input("Ingrese la hora de entrada del vehiculo: "))
minutoentrada = int(input("Ingrese el minuto de entrada del vehiculo: "))
horasalida = int(input("Ingrese la hora de salida del vehiculo: "))
minutosalida = int(input("Ingrese el minuto de salida del vehiculo: "))
horas = horasalida - horaentrada
minutos = minutosalida - minutoentrada
if minutos < 0:
    horas = horas - 1
    minutos = minutos + 60
print("El tiempo de estacionamiento es de", horas, "horas y", minutos, "minutos")
#:D
