def encontrar_maximo_minimo(lista):
    if len(lista) == 0:
        return None, None
    maximo = minimo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    return maximo, minimo

def main():
    numeros = []
    while True:
        entrada = input("Introduce un número (o 'q' para salir): ")
        if entrada == 'q':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    maximo, minimo = encontrar_maximo_minimo(numeros)
    
    if maximo is not None and minimo is not None:
        print(f"El valor máximo es: {maximo}")
        print(f"El valor mínimo es: {minimo}")
    else:
        print("La lista está vacía, no se puede determinar máximo y mínimo.")

if __name__ == "__main__":
    main()
