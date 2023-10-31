def k(n, p):
    if n == 0:
        return 0
    else:
        return n * p + k(n - 1, p)

# Ejemplo de uso
n = int(input("Ingrese n: "))
p = int(input("Ingrese p: "))
resultado = k(n, p)
print(f"K({n}, {p}) = {resultado}")
