#Variables
espaesta = [
    [0,1,0,0,1],
    [1,0,0,1,0],
    [0,0,1,0,0],
    [1,1,0,0,0]
] #Matriz
fila = 4 #int
espacio = 5 #int
#Codigo
print("Esta es la distribucion del estacionamiento: ")
for i in range(fila):
    for j in range(espacio):
        print(espaesta[i][j], end="")
    print()