
def flatten_list(lista):
    resultado = []
    for item in lista:
        if isinstance(item, list):
            resultado.extend(flatten_list(item))
        else:
            resultado.append(item)
    return resultado

mi_listaplana = [1, [2, [3, 4], 5]]
print("Lista aplanada:", flatten_list(mi_listaplana))