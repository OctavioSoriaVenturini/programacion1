def calcular_frecuencia_digito(numero, digito):
    """
    Calcula la frecuencia de un dígito en un número.

    Args:
        numero (int): El número en el que se busca el dígito.
        digito (int): El dígito que se busca.

    Returns:
        int: La cantidad de ocurrencias del dígito en el número.
    """
    frecuencia = str(numero).count(str(digito))
    return frecuencia

def main():
    try:
        numero = int(input("Ingresa un número entero: "))
        digito = int(input("Ingresa un dígito que deseas contar: "))

        if 0 <= digito <= 9:
            frecuencia = calcular_frecuencia_digito(numero, digito)
            print(f"El dígito {digito} aparece {frecuencia} veces en el número {numero}.")
        else:
            print("Por favor, ingresa un dígito válido (0-9).")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    main()
