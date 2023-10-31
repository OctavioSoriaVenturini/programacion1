def tamano_papel_A(n):
    if n == 0:
        return (841, 1189)
    else:
        ancho, largo = tamano_papel_A(n - 1)
        return largo, ancho / 2

# Ejemplo de uso
n = 3
ancho, largo = tamano_papel_A(n)
print(f"El tamaño de papel A{n} es: {ancho}mm x {largo}mm")
