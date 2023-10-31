def encontrar_posiciones(a, b, inicio=0):
    """
    Encuentra las posiciones en donde se encuentra b dentro de a.

    Args:
        a (str): Cadena de texto.
        b (str): Subcadena a buscar.
        inicio (int): Índice de inicio para la búsqueda (por defecto es 0).

    Returns:
        list: Lista de posiciones donde se encuentra b.
    """
    if inicio >= len(a):
        return []
    if a.find(b, inicio) == -1:
        return []
    return [a.find(b, inicio)] + encontrar_posiciones(a, b, a.find(b, inicio) + 1)

# Ejemplo de uso
cadena_a = "abracadabra"
subcadena_b = "ra"
posiciones = encontrar_posiciones(cadena_a, subcadena_b)
print(f"Las posiciones de '{subcadena_b}' en '{cadena_a}' son: {posiciones}")
