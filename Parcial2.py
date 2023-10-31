#OctavioSoria Comision 'C'- Parcial 2.

def is_mutant(dna):
    # Función para verificar si hay una secuencia en una dirección específica
    def check_sequence(x, y, dx, dy):
        base = dna[x][y]
        count = 1
        for i in range(1, 4):
            nx, ny = x + i*dx, y + i*dy
            if 0 <= nx < 6 and 0 <= ny < 6 and dna[nx][ny] == base:
                count += 1
            else:
                break
        return count >= 4

    # Verificar horizontal
    for i in range(6):
        for j in range(3):
            if check_sequence(i, j, 0, 1):
                return True

    # Verificar vertical
    for i in range(3):
        for j in range(6):
            if check_sequence(i, j, 1, 0):
                return True

    # Verificar diagonales hacia arriba
    for i in range(3):
        for j in range(3, 6):
            if check_sequence(i, j, 1, -1):
                return True

    # Verificar diagonales hacia abajo
    for i in range(3):
        for j in range(3):
            if check_sequence(i, j, 1, 1):
                return True

    return False

# Pedir al usuario que ingrese las secuencias de ADN
adn = []
for i in range(6):
    while True:
        fila = input(f"Ingrese la fila {i+1} de la secuencia de ADN: ")
        if fila:
            adn.append(fila)
            break
        else:
            print("No se ha ingresado nada. Por favor, intenta de nuevo.")


# Verificar si es mutante y mostrar el resultado
es_mutante = is_mutant(adn)
if es_mutante:
    print("El humano es mutante")
else:
    print("El humano no es mutante")
