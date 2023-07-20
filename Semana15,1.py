print()
print("== Valores pares ==")
print()
SUMA=0
CANT=0
for x in range(20,401):
    if (x % 2==0):
        SUMA=SUMA+x
        CANT=CANT+1
        print(x, end='-')
PROM=round(SUMA/CANT,2)
print()
print(f"La suma es {SUMA}")
print(f"su promedio es {PROM}")
print()