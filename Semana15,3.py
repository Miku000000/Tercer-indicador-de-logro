print()
print("Calcular la sucesion de los digitos")
print()
N=int(input("hasta que elemento de la recta quiere llegar: "))
SUMA=0
DATO=0
for x in range(1,N):
    if (x==1):
        DATO=1
    elif (x%2==0):
        DATO+=4
    else:
        DATO-=2
    SUMA=SUMA+DATO
if (N>0):
    print()
    print(f"La suma de su operacion es {SUMA} del orden {N}")
print()