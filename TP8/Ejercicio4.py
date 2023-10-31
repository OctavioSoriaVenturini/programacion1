def par(n):
    if n == 0:
        return True
    else:
        return impar(n - 1)

def impar(n):
    if n == 0:
        return False
    else:
        return par(n - 1)

# Ejemplo de uso
numero = 7
print(f"{numero} es par: {par(numero)}")
print(f"{numero} es impar: {impar(numero)}")
