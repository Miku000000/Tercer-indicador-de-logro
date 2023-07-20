print()
print("=Valores de 10==")
print()
SUMA=0
MA10=0
ME10=0
IG10=0
for x in range(1,11):
    NUM=int(input(f"DATO {x} <<"))
    SUMA=SUMA+NUM
    if (NUM>10):
        MA10+=1
    else:
        if (NUM<10):
            ME10+=1
        else:
            IG10+=1
ME=round(SUMA/10,2)
print(f"La cantidad de numeros menores a 10 seleccionados es {ME10}")
print(f"La cantidad de numeros mayores a 10 seleccionados es {MA10}")
print(f"Los numeros iguales a los numeros seleccionados son {IG10}")
print(f"La media de los numeros seleccionados son {ME}")