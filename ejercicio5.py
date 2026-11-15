# Ejercicio 5: Aplica un 10% de descuento si el vehiculo tiene mas de 10 visitas
#Variables
pago = 0.0 #float
visitas = 0 #int
pagof = 0.0 #float
#Codigo
pago = float(input("Ingrese el pago por el tiempo de estacionamiento: "))
visitas = int(input("Ingrese el numero de visitas del vehiculo: "))
if visitas > 10:
    pagof = pago * 0.9
    visitas = 0
print("El pago final por el tiempo de estacionamiento es de: $", pagof)
#:D
