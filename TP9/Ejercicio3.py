class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def mayor_lado(self):
        return max(self.lado1, self.lado2, self.lado3)
    
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

# Función para obtener un valor numérico desde el usuario
def obtener_valor(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Por favor, ingresa un valor positivo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Solicitar al usuario los lados del triángulo
lado1 = obtener_valor("Ingresa el primer lado del triángulo: ")
lado2 = obtener_valor("Ingresa el segundo lado del triángulo: ")
lado3 = obtener_valor("Ingresa el tercer lado del triángulo: ")

# Crear un objeto de la clase Triangulo
triangulo = Triangulo(lado1, lado2, lado3)

# Mostrar el lado con mayor tamaño y el tipo de triángulo
print(f"El lado con mayor tamaño es: {triangulo.mayor_lado()}")
print(f"El triángulo es de tipo: {triangulo.tipo_triangulo()}")
