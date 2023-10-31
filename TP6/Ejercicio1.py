numbers = []

while True:
    number = int(input("Ingrese un número (0 para finalizar): "))
    
    if number == 0:
        break  # Si el usuario ingresa 0, salimos del bucle
    else:
        numbers.append(number)  # Agregar el número a la lista

# Mostrar los números ingresados
print("Números ingresados:", numbers)