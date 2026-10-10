"""4. **Caminos en un Tablero**: Escribe una función recursiva que calcule el número de caminos posibles desde la esquina superior izquierda (0,0) hasta la inferior derecha de una matriz NxM, asumiendo que solo puedes moverte hacia abajo o a la derecha. *Acompaña con análisis Big-O.*"""
def caminos_tablero(n, m, memo=None):
    if memo is None:
        memo = {}
    if n == 1 or m == 1:
        return 1
    if (n, m) in memo:
        return memo[(n, m)]
    
    memo[(n, m)] = caminos_tablero(n - 1, m, memo) + caminos_tablero(n, m - 1, memo)
    return memo[(n, m)]

filas = int(input("Ingresa el número de filas (N): "))
columnas = int(input("Ingresa el número de columnas (M): "))

print("Número total de caminos:", caminos_tablero(filas, columnas))