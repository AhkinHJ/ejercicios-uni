# Ejercicio 1: Registra los datos de un vehiculo (placa, propietario y hora de entrada)
#Variables
placa = "" #string
nombre = "" #string
hora = 0 #int
minuto = 0 #int
#Codigo
placa = input("Ingrese la placa del vehiculo: ")
nombre = input("Ingrese el nombre del propietario: ")
hora = int(input("Ingrese la hora de entrada del vehiculo: "))
minuto = int(input("Ingrese el minuto de entrada del vehiculo: "))
print("\nDatos del vehiculo:")
print("Placa:", placa)
print("Propietario:", nombre)
print("Hora de entrada:", hora, "horas y", minuto, "minutos")
#:D
