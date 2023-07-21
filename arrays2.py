print()
print("HAllar la suma del array 100")
print()
AR = []
SUMA=0
for x in range (0,10):
    AR.append(int(input(f"DATO {x+1}: ")))
for x in range (len(AR)):
    print(AR[x], end="|")
    SUMA+=AR[x]
MEDIA=SUMA/100
print()
print(f"La suma de su array es {SUMA}")
print(f"La media de su array es {MEDIA}")
print()