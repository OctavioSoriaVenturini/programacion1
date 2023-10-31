# Definimos una función llamada agregar_espacio que toma un texto como parámetro.
def agregar_espacio(texto):
    # Usamos el método join para unir todos los caracteres del texto con un espacio en blanco entre ellos.
    
    return ' '.join(texto)

# Creamos una variable llamada texto y le asignamos el valor "Hola, tú".
texto = input("Ingrese un texto: ")

# Llamamos a la función agregar_espacio y le pasamos el texto como argumento.
# El resultado de la función se guarda en la variable resultado.
resultado = agregar_espacio(texto)

# Imprimimos el resultado.
print(resultado)