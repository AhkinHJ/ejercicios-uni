# Ejercicio 15: Estadisticas de ocupacion del estacionamiento
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
ocupados = 0 #int
libre = 0 #int
op = 1 #int
porcent = 0.0 #float
totespa = 20 #int
i = 0 #int
j = 0 #int
#Codigo
while op != 0:
    op = int(input("\nIngrese una opcion:\n1. Numero total de espacio\n2. Numero de espacios ocupados\n3. Numero de espacios libres\n4. Porcentaje de ocupacion\n0. Salir.\n"))
    match op:
        case 1:
            print("El total de espacios es: ", totespa)
        case 2:
            ocupados = 0
            for i in range(fila):
                for j in range(espacio):
                    if espaesta[i][j] == 1:
                        ocupados = ocupados + 1
            print("Los espacios ocupados son: ", ocupados)
        case 3:
            libre = 0
            for i in range(fila):
                for j in range(espacio):
                    if espaesta[i][j] == 0:
                        libre = libre + 1
            print("Los espacios libres son: ", libre)
        case 4:
            ocupados = 0
            for i in range(fila):
                for j in range(espacio):
                    if espaesta[i][j] == 1:
                        ocupados = ocupados + 1
            porcent = (ocupados*100)/totespa
            print("El porcentaje de espacios ocupados son: $", porcent)
        case 0:
            print("Saliendo...")
        case _:
            print("Opcion no valida.")
#:D
