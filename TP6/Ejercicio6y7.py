# Ejercicio 6
def obtener_nombres_nivel():
    nombres = set()
    while True:
        nombre = input("Ingresa un nombre (o 'x' para salir): ")
        if nombre == 'x':
            break
        nombres.add(nombre)
    return nombres

print("Nivel Primario:")
nombres_primario = obtener_nombres_nivel()

print("\nNivel Secundario:")
nombres_secundario = obtener_nombres_nivel()

# a. Informar los nombres sin repeticiones
print("\nNombres de nivel primario sin repeticiones:")
print(nombres_primario)

print("\nNombres de nivel secundario sin repeticiones:")
print(nombres_secundario)

# b. Nombres repetidos
nombres_repetidos = nombres_primario.intersection(nombres_secundario)
print("\nNombres repetidos entre primario y secundario:")
print(nombres_repetidos)

# c. Nombres de primario que no se repiten en secundario
nombres_primario_no_repetidos = nombres_primario - nombres_secundario
print("\nNombres de nivel primario no repetidos en secundario:")
print(nombres_primario_no_repetidos)

# Ejercicio 7
ocurrencias = {}

for _ in range(50):
    string = input("Ingresa un string: ")
    for char in string:
        ocurrencias[char] = ocurrencias.get(char, 0) + 1

print("\nOcurrencias de cada carácter:")
for char, count in ocurrencias.items():
    print(f"'{char}': {count}")
