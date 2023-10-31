def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    # Dividir la lista en mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # Aplicar recursivamente el merge sort a las mitades
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    # Combinar las mitades ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []

    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado

# Ejemplo de uso
lista_numeros = [8, 3, 1, 7, 0, 5, 9, 2, 6, 4]
lista_ordenada = merge_sort(lista_numeros)
print(lista_ordenada)
