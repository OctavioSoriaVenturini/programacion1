def encontrar_mayor(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        max_resto = encontrar_mayor(lista[1:])
        return lista[0] if lista[0] > max_resto else max_resto

# Ejemplo de uso
lista_numeros = [5, 3, 9, 1, 7, 2, 8]
mayor = encontrar_mayor(lista_numeros)
print(f"El mayor elemento de la lista es: {mayor}")
