def obtener_diagonal_principal(matriz):
    return [matriz[i][i] for i in range(len(matriz))]

def obtener_diagonal_inversa(matriz):
    return [matriz[i][len(matriz)-1-i] for i in range(len(matriz))]

# Ejemplo de uso
matriz_ejemplo = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

print("Diagonal principal:", obtener_diagonal_principal(matriz_ejemplo))
print("Diagonal inversa:", obtener_diagonal_inversa(matriz_ejemplo))
