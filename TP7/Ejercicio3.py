# Crear una lista de diccionarios con información sobre libros
libros = [
    {'título': 'El Aleph', 'autor': 'Jorge Luis Borges', 'año': 1949},
    {'título': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'año': 1967},
    {'título': '1984', 'autor': 'George Orwell', 'año': 1949},
    {'título': 'Don Quijote de la Mancha', 'autor': 'Miguel de Cervantes', 'año': 1605},
    {'título': 'Moby Dick', 'autor': 'Herman Melville', 'año': 1851},
]

def ordenar_por_ano(libro):
    return libro['año']

def ordenar_por_autor(libro):
    return libro['autor']

# Ordenar la lista de libros por año de publicación
libros_ordenados_por_ano = sorted(libros, key=ordenar_por_ano)

# Mostrar la lista de libros ordenados por año de publicación
print("Libros ordenados por año de publicación:")
for libro in libros_ordenados_por_ano:
    print(libro)

# Ordenar la lista de libros por autor
libros_ordenados_por_autor = sorted(libros, key=ordenar_por_autor)

# Mostrar la lista de libros ordenados por autor
print("\nLibros ordenados por autor:")
for libro in libros_ordenados_por_autor:
    print(libro)
