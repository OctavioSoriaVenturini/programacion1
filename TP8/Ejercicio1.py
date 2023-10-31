def contar_digitos(n):
    """
    Cuenta la cantidad de dígitos en un número positivo.

    Args:
        n (int): Número positivo.

    Returns:
        int: Cantidad de dígitos en el número.
    """
    if n == 0:
        return 1
    else:
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count

# Ejemplo de uso
numero = 12345
cantidad_digitos = contar_digitos(numero)
print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
