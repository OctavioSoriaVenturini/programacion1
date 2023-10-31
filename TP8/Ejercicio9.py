def combinaciones(lista, k, prefijo=""):
    if k == 0:
        print(prefijo)
        return
    for i in range(len(lista)):
        combinaciones(lista, k - 1, prefijo + lista[i])

# Ejemplo de uso
caracteres = ['a', 'b', 'c']
longitud = 2
combinaciones(caracteres, longitud)
