
'''TP 3 PROGRAMACIÓN I Octavio Soria.
ACLARACIONES: Las variables están en inglés, además todas están acompañadas de la abreviatura en inglés: "ex" (exercise, ejercicio en español). acompañado del número del ejercicio que hace referencia el código. ej: var_ex_1
 '''

'''1. Create a while loop with the following characteristics:

• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x was ' + x.
• The console output should look like this'''

x_ex_1 = 0
while x_ex_1 <= 30:
    x_ex_1 += 1
    if x_ex_1 == 15:
        print('La ejecución del loop fue interrumpida cuando x valía: ' , x_ex_1)
        break

    if x_ex_1 == 4 or x_ex_1 == 6 or x_ex_1 == 10:
        print("El valor " , x_ex_1, " de x fue salteado");
    else: 
        print('El valor del loop es: ',x_ex_1)

# 2.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.
phrases_ex_2 = []

# Lee las líneas hasta que se ingrese una línea en blanco
while True:
    phrase_ex_2 = input("Ingrese una línea (deje en blanco para finalizar): ")
    if phrase_ex_2:
        # Agrega la línea a la lista
        phrases_ex_2.append(phrase_ex_2)
    else:
        # Si se ingresa una línea en blanco, sal del bucle
        break

# Convierte todas las líneas a mayúsculas e imprímelas
for phrase_ex_2 in phrases_ex_2:
    print(phrase_ex_2.upper())

'''3.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50

D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos

Ejemplo de una entrada:
D 200
D 200
R 100
D 50
Introducir una línea vacía indica que ha finalizado la bitácora.
La salida de éste programa sería:
350'''

total_ex_3 = 0
input("D = Depositar, R= Retirar. Si no desea ingresar o retirar dinero coloque 0. Si desea terminar la ejecución ingrese un lugar vacío con enter")
while True:
    deposit_ex_3 = input("D ")
    withdraw_ex_3 = input("R ")
    
    # Verifica si el usuario presionó Enter sin ingresar ningún valor
    if deposit_ex_3 == "" or withdraw_ex_3 == "":
        print("Su total actual es:", total_ex_3 )
        break
    
    # Convierte las entradas en números flotantes
    deposit_ex_3 = float(deposit_ex_3) if deposit_ex_3 else 0
    withdraw_ex_3 = float(withdraw_ex_3) if withdraw_ex_3 else 0
    
    # Calcula el saldo
    total_ex_3 = deposit_ex_3 - withdraw_ex_3

'''4.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
Imprimir la cantidad total de números primos ingresados.
Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.
'''
print("Ingrese números mayores a 0, enteros. Ingrese 0 para terminar la ejecución.")
prime_ex_4 = []

while True:
    numbers_ex_4 = int(input())
    
    if numbers_ex_4 == 0:
        break
    
    is_prime_ex_4 = True
    
    if numbers_ex_4 <= 1:
        is_prime_ex_4 = False
    else:
        for i_ex_4 in range(2, int(numbers_ex_4 ** 0.4) + 1):
            if numbers_ex_4 % i_ex_4 == 0:
                is_prime_ex_4 = False
                break
    
    if is_prime_ex_4:
        prime_ex_4.append(numbers_ex_4)

print("Los números primos ingresados son:", prime_ex_4)   

'''5.	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
'''
import sys

print("Ingrese dos años distintos: (El primero debe ser menor al segundo)")
year1_ex_5 = int(input())
year2_ex_5 = int(input())
leap_year_ex_5 = []
divisible_10 = []

while True: 
    if year1_ex_5 > year2_ex_5:
        print("El primer año ingresado debe ser menor al segundo: ")
        sys.exit()


    for i_ex_5 in range(year1_ex_5, year2_ex_5 + 1):
        if (i_ex_5 % 4 == 0 and i_ex_5 % 100 != 0) or (i_ex_5 % 400 == 0):
            leap_year_ex_5.append(i_ex_5)
        
        if i_ex_5 % 10 == 0:
                divisible_10.append(i_ex_5)
    if i_ex_5 == year2_ex_5:
        break

print("Los años bisiestos en el rango de años son:", leap_year_ex_5)
print("Los años divisibles por 10 pero que no son bisiestos en el rango de años son:", divisible_10)

'''# 6.	Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración continue para omitir los números impares.'''
for numero_ex_6 in range(1, 21):
    if numero_ex_6 % 2 != 0:  # Verifica si el número es impar
        continue  # Omite los números impares
    print(numero_ex_6)  # Imprime los números pares

'''6.	Crea una lista de números y utiliza un bucle for para encontrar un número específico. Cuando encuentres el número, usa break para salir del bucle.'''

# Lista de números
numbers_ex_7 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Número específico que deseas encontrar
target_number_ex_7 = 60

# Bucle for para buscar el número
for number_ex_7 in numbers_ex_7:
    if number_ex_7 == target_number_ex_7:
        print(f"¡Encontré el número {target_number_ex_7}!")
        break  # Salir del bucle cuando encuentres el número

# Este mensaje se imprimirá después de salir del bucle
print("Bucle finalizado.")

'''7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).
'''

while True:
    # Mostrar el menú de opciones
    print("Menú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("0. Salir del programa")

    # Solicitar al usuario que elija una opción
    option_ex_8 = input("Seleccione una opción: ")

    # Verificar la opción ingresada por el usuario
    if option_ex_8 == "1":
        print("Ha elegido la Opción 1")
    elif option_ex_8 == "2":
        print("Ha elegido la Opción 2")
    elif option_ex_8 == "3":
        print("Ha elegido la Opción 3")
    elif option_ex_8 == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
