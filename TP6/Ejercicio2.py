numbers = []

# Solicitar al usuario que ingrese números, 0 para finalizar
while True:
    number = int(input("Ingrese un número (0 para finalizar): "))
    
    if number == 0:
        break
    else:
        numbers.append(number)

# Mostrar los números ingresados
print("Números ingresados:", numbers)

# Solicitar al usuario que ingrese un número a eliminar
number_to_delete = int(input("Ingrese el número que desea eliminar: "))

# Verificar si el número está en la lista y eliminar la primera ocurrencia
if number_to_delete in numbers:
    numbers.remove(number_to_delete)
    print(f"Se eliminó la primera ocurrencia del número {number_to_delete}.")
else:
    print(f"El número {number_to_delete} no está en la lista. No se pudo eliminar.")
    
# Mostrar la lista actualizada
print("Lista actualizada:", numbers)