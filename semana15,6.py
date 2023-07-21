print()
print("Pago del automovil por 20 meses")
print()
SUMA=0
PAGO=5
for x in range(1,21):
    PAGO*=2
    SUMA+=PAGO
    print(PAGO)
print()
print(f"La suma de sus pagos es {SUMA}")
print()