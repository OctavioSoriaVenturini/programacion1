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

def calcular_suma_digitos(numero):
    """
    Calcula la suma de los dígitos de un número.

    Args:
        numero (int): El número del cual se calculará la suma de dígitos.

    Returns:
        int: La suma de los dígitos.
    """
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

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

def calcular_factorial(numero):
    """
    Calcula el factorial de un número dado.

    Args:
        numero (int): El número para el cual se calculará el factorial.

    Returns:
        int: El factorial del número.
    """
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

def main():
    mayor_primo = -1

    while True:
        try:
            numero = int(input("Ingresa un número primo (o un número no primo para terminar): "))

            if numero < 0:
                print("Por favor, ingresa un número positivo.")
                continue

            if numero == 0:
                break

            if es_primo(numero):
                suma_digitos = calcular_suma_digitos(numero)
                print(f"La suma de los dígitos de {numero} es: {suma_digitos}")

                digito = int(input("Ingresa un dígito que deseas contar: "))
                frecuencia = calcular_frecuencia_digito(numero, digito)
                print(f"El dígito {digito} aparece {frecuencia} veces en el número {numero}.")

                if numero > mayor_primo:
                    mayor_primo = numero
            else:
                print(f"{numero} no es un número primo. Programa terminado.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    if mayor_primo != -1:
        factorial_mayor_primo = calcular_factorial(mayor_primo)
        print(f"El factorial del mayor número primo ingresado ({mayor_primo}) es: {factorial_mayor_primo}")

if __name__ == "__main__":
    main()
