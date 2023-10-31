def replicar(lista, n):
    if n == 0:
        return []
    else:
        return lista + replicar(lista, n - 1)

# Ejemplo de uso
lista_original = [1, 3, 3, 7]
replicada = replicar(lista_original, 2)
print(f"Lista replicada: {replicada}")
