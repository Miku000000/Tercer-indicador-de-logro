print()
print("Bucle hasta que se ingrese el numero cero")
print()
SUMA=0
C=0
NUM=float(input("DATO 1: "))
while (NUM!=0):
    SUMA+=NUM
    C+=1
    NUM=float(input(F"DATO {C+1}: "))
if(C>0):
    MEDIA=round(SUMA/C,2)
    print()
    print(f"La suma de los datos es ({SUMA}) y la media es ({MEDIA})")
    print()
else:
    print("No se ingreso ningun valor valido")