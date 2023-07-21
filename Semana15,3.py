print()
print("Calcular la sucesion de los digitos")
print()
N=int(input("hasta que elemento de la recta quiere llegar: "))
if(N>0):
    SUMA=0
    DATO=0
    for x in range(1,N+1):
        if (x==1):
            DATO=1
        elif (x%2==0):
            DATO+=4
        else:
            DATO-=2
        SUMA=SUMA+DATO
        print(DATO, end="|")
    print()
    print()
    print(f"La suma de su operacion es {SUMA}")
    print()
else:
    print()
    print(f"ERROR el dato {N} es incorrecto pruebe los datos de 1 en adelante")
    print()