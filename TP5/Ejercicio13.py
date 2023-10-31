import math

def calcular_modulo_vector(x, y, z):
    """
    Calcula el módulo de un vector en un espacio euclidiano tridimensional.

    Args:
        x (float): Componente en el eje x.
        y (float): Componente en el eje y.
        z (float): Componente en el eje z.

    Returns:
        float: Módulo del vector.
    """
    modulo = math.sqrt(x**2 + y**2 + z**2)
    return modulo

def main():
    try:
        x = float(input("Ingresa la componente en el eje x: "))
        y = float(input("Ingresa la componente en el eje y: "))
        z = float(input("Ingresa la componente en el eje z: "))

        modulo = calcular_modulo_vector(x, y, z)

        print(f"El módulo del vector ({x}, {y}, {z}) es: {modulo}")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()
