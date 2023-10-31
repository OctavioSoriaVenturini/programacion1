def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

# Ejemplo de uso
fila = 5
columna = 2
valor = pascal(fila, columna)
print(f"El valor en la fila {fila}, columna {columna} es: {valor}")
