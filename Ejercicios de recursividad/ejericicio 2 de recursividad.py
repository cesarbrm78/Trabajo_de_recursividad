"""2. **Conteo de Vocales**: Cuenta el número de vocales en un string recursivamente."""
def contar_vocales(texto):
    if not texto:
        return 0
    
    vocales = "A,E,I,O,U,a.e.i.o.u"
    es_vocal = 1 if texto[0] in vocales else 0
    
    return es_vocal + contar_vocales(texto[1:])

texto_usuario = input("Ingresa un texto o una palabra: ")
print("Número de vocales:", contar_vocales(texto_usuario))