import random

def crear_tablero(filas, columnas):
    numeros = list(range(1, (filas*columnas)//2 + 1))
    cartas = numeros + numeros
    random.shuffle(cartas)
    return [[cartas.pop() for _ in range(columnas)] for _ in range(filas)]

def mostrar_tablero(tablero, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            if tablero[i][j] == 0:
                print('* ', end='')
            else:
                print(f'{tablero[i][j]} ', end='')
        print()

def destapar_carta(tablero, fila, columna):
    return tablero[fila][columna]

def main():
    filas = int(input("Ingresa el número de filas del tablero: "))
    columnas = int(input("Ingresa el número de columnas del tablero: "))

    tablero = crear_tablero(filas, columnas)
    destapadas = [[False for _ in range(columnas)] for _ in range(filas)]

    while True:
        mostrar_tablero(tablero, filas, columnas)
        fila1 = int(input("Ingresa la fila de la primera carta: "))
        columna1 = int(input("Ingresa la columna de la primera carta: "))
        fila2 = int(input("Ingresa la fila de la segunda carta: "))
        columna2 = int(input("Ingresa la columna de la segunda carta: "))

        carta1 = destapar_carta(tablero, fila1, columna1)
        carta2 = destapar_carta(tablero, fila2, columna2)

        if carta1 == carta2 and (fila1 != fila2 or columna1 != columna2) and not destapadas[fila1][columna1] and not destapadas[fila2][columna2]:
            print("¡Has encontrado una pareja!")
            destapadas[fila1][columna1] = True
            destapadas[fila2][columna2] = True
        else:
            print("Las cartas no coinciden o ya han sido seleccionadas.")

        if all(all(fila) for fila in destapadas):
            print("¡Has ganado!")
            break

if __name__ == "__main__":
    main()
