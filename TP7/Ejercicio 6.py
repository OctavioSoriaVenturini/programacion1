def counting_sort(arr):
    max_value = max(arr)
    count_array = [0] * (max_value + 1)

    for num in arr:
        count_array[num] += 1

    sorted_array = []
    for i in range(len(count_array)):
        sorted_array.extend([i] * count_array[i])

    return sorted_array

# Solicitar al usuario que ingrese los números
lista_desordenada = []
print("Ingresa números enteros (escribe 'fin' para terminar):")
while True:
    entrada = input("> ")
    if entrada == 'fin':
        break
    try:
        num = int(entrada)
        lista_desordenada.append(num)
    except ValueError:
        print("Por favor, ingresa solo números enteros o 'fin' para terminar.")

# Ordenar la lista utilizando el algoritmo de ordenamiento por conteo
lista_ordenada = counting_sort(lista_desordenada)

# Imprimir la lista ordenada
print("Lista ordenada:", lista_ordenada)
