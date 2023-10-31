# Inicializar una lista para guardar los números ingresados
numbers = []

# Solicitar al usuario que ingrese números, 0 para finalizar
while True:
    number = int(input("Ingrese un número (0 para finalizar): "))
    
    if number == 0:
        break
    else:
        numbers.append(number)  # Agregar el número a la lista

# Mostrar los números ingresados
print("Números ingresados:", numbers)

# Solicitar al usuario que ingrese otro número
numero_limite = int(input("Ingrese otro número para filtrar la lista: "))

# Crear una nueva lista con elementos menores que el número dado
nueva_lista = [n for n in numbers if n < numero_limite]

# Mostrar la nueva lista iterando por ella
print("Nueva lista con elementos menores que", numero_limite, ":")
for elemento in nueva_lista:
    print(elemento)