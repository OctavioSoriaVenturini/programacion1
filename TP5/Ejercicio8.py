import math

def calcular_area_perimetro_circunferencia(radio):
    """
    Calcula el área y el perímetro de una circunferencia.

    Args:
        radio (float): El radio de la circunferencia.

    Returns:
        tuple: Una tupla que contiene el área y el perímetro en ese orden.
    """
    # Fórmula para el área de una circunferencia: pi * radio^2
    # Fórmula para el perímetro de una circunferencia: 2 * pi * radio
    area = math.pi * (radio**2)
    perimetro = 2 * math.pi * radio
    return area, perimetro

def main():
    try:
        # Solicita al usuario que ingrese el radio de la circunferencia
        radio = float(input("Ingresa el radio de la circunferencia: "))
        if radio >= 0:
            # Calcula el área y el perímetro
            area, perimetro = calcular_area_perimetro_circunferencia(radio)
            # Muestra el área y el perímetro en la consola
            print(f"El área de la circunferencia es: {area:.2f}")
            print(f"El perímetro de la circunferencia es: {perimetro:.2f}")
        else:
            print("El radio debe ser un valor positivo.")
    except ValueError:
        print("Por favor, ingresa un valor numérico válido para el radio.")

if __name__ == "__main__":
    main()
