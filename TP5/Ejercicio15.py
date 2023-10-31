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
    numeros_leidos = 0

    while True:
        try:
            numero = int(input("Ingresa un número (o 'q' para salir): "))
            if numero < 0:
                print("Por favor, ingresa un número no negativo.")
            else:
                factorial = calcular_factorial(numero)
                print(f"El factorial de {numero} es: {factorial}")
                numeros_leidos += 1
        except ValueError:
            entrada = input("No has ingresado un número. ¿Quieres salir? (s/n): ")
            if entrada.lower() == 's':
                break

    print(f"Se leyeron un total de {numeros_leidos} números.")

if __name__ == "__main__":
    main()
