def es_primo(numero):
    """
    Verifica si un número dado es primo.

    Args:
        numero (int): El número que se desea verificar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main():
    try:
        numero = int(input("Ingresa un número entero: "))
        if es_primo(numero):
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    main()