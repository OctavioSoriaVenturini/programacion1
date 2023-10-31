def es_potencia(n, b):
    """
    Verifica si n es potencia de b.

    Args:
        n (int): Número entero.
        b (int): Base.

    Returns:
        bool: True si n es potencia de b, False en caso contrario.
    """
    if n == 1:
        return True
    if n % b != 0 or n == 0:
        return False
    return es_potencia(n // b, b)

# Ejemplo de uso
numero = 8
base = 2
resultado = es_potencia(numero, base)
print(f"{numero} es potencia de {base}: {resultado}")
