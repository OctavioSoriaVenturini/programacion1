# Crear una lista que contenga números y cadenas de caracteres
lista_mixta = [10, 'manzana', 5, 'naranja', 2, 'pera', 'banana', 7]

# Separar los números y las cadenas
numeros = [elemento for elemento in lista_mixta if isinstance(elemento, (int, float))]
cadenas = [elemento for elemento in lista_mixta if isinstance(elemento, str)]

# Ordenar los números de menor a mayor
numeros_ordenados = sorted(numeros)

# Ordenar las cadenas alfabéticamente
cadenas_ordenadas = sorted(cadenas)

# Combinar las listas ordenadas
lista_ordenada = numeros_ordenados + cadenas_ordenadas

# Mostrar la lista ordenada
print(lista_ordenada)
