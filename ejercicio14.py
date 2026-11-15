# Ejercicio 14: Estaciona un vehiculo en una fila y espacio de la matriz
#Variables
espaesta = [
    [0,1,0,0,1],
    [1,0,0,1,0],
    [0,0,1,0,0],
    [1,1,0,0,0]
] #Matriz
fila = 4 #int
espacio = 5 #int
fibus = 0 #int
espaciobus = 0 #int
i = 0 #int
j = 0 #int
#Codigo
print("Esta es la distribucion del estacionamiento: ")
for i in range(fila):
    for j in range(espacio):
        print(espaesta[i][j], end="")
    print()
fibus = int(input("\nLa fila en la que se va a estacionar el carro: "))
fibus = fibus - 1
espaciobus = int(input("El pacio en el que se va a estacionar el carro: "))
espaciobus = espaciobus - 1
if espaesta[fibus][espaciobus] == 1:
    print("El espacio esta ocupado")
else:
    print("Se puede estacionar. Estacionado")
    espaesta[fibus][espaciobus] = 1
print("\nEspacios en el estacionamiento actualizados:")
for i in range(fila):
    for j in range(espacio):
        print(espaesta[i][j], end = "")
    print()
#:D
