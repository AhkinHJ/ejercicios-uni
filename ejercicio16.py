#variables
espaesta = [
    [0,1,0,0,1],
    [1,0,0,1,0],
    [0,0,1,0,0],
    [1,1,0,0,0]
] #Matriz
fila = 4 #int
espacio = 5 #int
filmay = 0 #int
mayocup = 0 #int
ocupados = 0 #int
libres = 0 #int
#Codigo
for i in range(fila):
    ocupados = 0
    for j in range(espacio):
        if espaesta[i][j] == 1:
            ocupados = ocupados + 1
    libres = espacio - ocupados
    print("Fila ", i + 1, ": ocupados = ", ocupados, ", libres = ", libres)
    if ocupados > mayocup:
        mayocup = ocupados
        filmay = i + 1
print("\nLa fila con mayor cantidad de vehiculos es la fila ", filmay, " con ", mayocup, " vehiculos.") 
