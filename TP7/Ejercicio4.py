def insertion_sort_by_length(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and len(key) < len(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Solicitar al usuario que ingrese las cadenas
lista_cadenas = []
print("Ingrese palabras (escribe 'fin' para terminar):")
while True:
    entrada = input("> ")
    if entrada == 'fin':
        break
    lista_cadenas.append(entrada)

# Ordenar la lista de cadenas por longitud utilizando el método de ordenamiento de inserción
insertion_sort_by_length(lista_cadenas)

# Imprimir la lista ordenada por longitud
print("Lista ordenada por longitud:", lista_cadenas)
