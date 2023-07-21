print()
print("Array del 1 al 100")
print()
AR = []
SUMA=0
for x in range (0,10000):
    AR.append(x+1)
for x in range (len(AR)):
    print(AR[x], end="|")
    SUMA+=AR[x]
MEDIA=SUMA/100
print()
print()
print(f"La suma es: {SUMA}")
print(f"La media es: {MEDIA}")
print()