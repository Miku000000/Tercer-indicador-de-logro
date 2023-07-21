print()
print("Verificacion de automoviles")
print()
SUMA=0
CANT=0
while True:
    Puntos=float(input(f"Ingresa los puntos contaminantes {CANT+1}: "))
    SUMA+=Puntos
    CANT+=1
    if(CANT==1):
        MA=Puntos
        ME=Puntos
    elif (Puntos>MA):
        MA=Puntos
    else:
        ME=Puntos
    RPTA=input("Desea registrar un nuevo automovil(SI)(NO):").upper()
    if(RPTA!="SI"):
        break
PROM=round(SUMA/CANT,2)
print()
print(f"El promedio de puntos contaminantes es {PROM} la cantidad de numeros mayores es {MA} y la cantidad de numeros menores es {ME}")
print()