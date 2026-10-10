"""**Imprimir Patrón**: Dado un número `n`, imprime usando recursividad un patrón de asteriscos. Ejemplo para n=3:"""
def imprimir_asteriscos(cantidad):
    if cantidad <= 0:
        return
    print("*", end="")
    imprimir_asteriscos(cantidad - 1)

def imprimir_patron(n, actual=1):
    if actual > n:
        return
    imprimir_asteriscos(actual)
    print() 
    imprimir_patron(n, actual + 1)

num = int(input("Ingresa un número: "))
imprimir_patron(num)