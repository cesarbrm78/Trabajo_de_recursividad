"""1. **Multiplicación Rusa (sin operador `*`)**: Implementa una función recursiva que multiplique dos números `a` y `b` usando únicamente sumas. *Acompaña con análisis Big-O.*"""
def multiplicacion_rusa(a, b):
    if b == 0:
        return 0
    if b % 2 == 0:
        return multiplicacion_rusa(a + a, b // 2)
    else:
        return a + multiplicacion_rusa(a + a, b // 2)

num1 = int(input("Ingresa tu primer numero: "))
num2 = int(input("Ingresa tu segundo numero: "))

print("Resultado:", multiplicacion_rusa(num1, num2))