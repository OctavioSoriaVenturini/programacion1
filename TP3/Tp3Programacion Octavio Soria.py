'''TP 3 PROGRAMACIÓN I Octavio Soria.
ACLARACIONES: Las variables están en inglés, además todas están acompañadas de la abreviatura en inglés: "ex" (exercise, ejercicio en español). acompañado del número del ejercicio que hace referencia el código. ej: var_ex_1
 '''
import math

# 1-	Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.


word_ex_1 =  str(input("Ingrese una palabra: "))

for i_ex_1 in range (10):
    print (word_ex_1, " ", end="")


# 2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


age_ex_2= int(input("Ingrese su edad: "))
for i_ex_2 in range(1,age_ex_2 + 1,1):
    print("año: ", i_ex_2)


# 3. Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


number_1_ex_3 = int(input("ingrese un numero entero positivo: "))
number_2_ex_3 = 1

for i_ex_3 in range (1, number_1_ex_3+1 ,2):
    if not ((i_ex_3 % 2) == 0):
        print (i_ex_3, end=", ")
        

# 4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.


number_ex_4= int(input("Ingrese un número entero positivo: "))

for i_ex_4 in range (number_ex_4, 0 ,-1):
    print(i_ex_4, end=", ")
print(0)


# 5-	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.


initial_capital_ex_5 = float(input("Ingrese su capital inicial: "))
anual_interest_ex_5 = float(input("Ingrese el % del interés generado anualmente: "))
years_to_investment_ex_5 = int(input("Ingrese los años a invertir: "))

if initial_capital_ex_5 > 0 and anual_interest_ex_5 >= 0 and years_to_investment_ex_5 > 0:
    for i_ex_5 in range(1, years_to_investment_ex_5 + 1):
        return_ex_5 = initial_capital_ex_5 * (1 + anual_interest_ex_5 / 100)**i_ex_5
        print(f"Capital obtenido en el año {i_ex_5}: {return_ex_5:.2f} $")
else:
    print("Datos incorrectos")


# 6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.


height_ex_6= int(input("Ingrese la altura del triángulo: "))

for i_ex_6 in range (1,height_ex_6 + 1):
    for j_ex_6 in range(0, i_ex_6 , 1): #También puedo pensarlo que parta desde el número de i_ex_6 y que vaya hasta 0, restandole 1 = for j_ex_6 in range(i_ex_6, 0 , 1)
        print("*",end="") #El end="" se lo agregamos porque por defecto el print mete un salto de línea
    print()


#7. Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.


for i_ex_7 in range (0, 10):
    i_ex_7=i_ex_7 +1
    for j_ex_7 in range (1, 11):
        result=(i_ex_7*j_ex_7)
        print(f"{i_ex_7} X {j_ex_7}= ", result )
        

# 8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.


number_ex_8= int(input("Ingrese un número entero positivo: "))

for i_ex_8 in range(1, number_ex_8 + 1):
    for j_ex_8 in range(i_ex_8, 0, -1):
        print(j_ex_8, end="")
    print()


# 9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

password_ex_9 = "contraseña"

password_petition_ex_9 = str(input("Ingrese su contraseña porfavor: "))
while password_petition_ex_9 != password_ex_9 :
    password_petition_ex_9 = str(input("Incorrecto, ingrese su contraseña porfavor: "))

print("Acceso permitido")


# 10-	Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.


import math

prime_number_ex_10 = int(input("Ingrese un número para saber si es primo o no: "))

if prime_number_ex_10 <= 1:
    print("No es un número primo")
elif prime_number_ex_10 == 2 or prime_number_ex_10 == 3:
    print("Es un número primo")
else: 
    es_primo_ex_10 = True
    for i_ex_10 in range(2, int(math.sqrt(prime_number_ex_10)) + 1):
        if prime_number_ex_10 % i_ex_10 == 0 :
            es_primo_ex_10 = False
            break

    if es_primo_ex_10:
        print(prime_number_ex_10, "es un número primo")
    else:
        print(prime_number_ex_10, "no es un número primo")


# 11.	Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.


word_ex_11 = str(input("Ingrese una palabra: "))

for i_ex_11 in reversed(word_ex_11):
    print(i_ex_11, end="")


# 12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

phrase_ex_12= str(input("Ingrese una frase: "))
letter_ex_12= str(input("Ingrese la letra que quiere buscar: "))
counter_ex_12=0

for i_ex_12 in phrase_ex_12: 
    if letter_ex_12==i_ex_12 :
        counter_ex_12= counter_ex_12 + 1
    
if counter_ex_12 > 0:
    print ("la cantidad de veces que aparece la letra es:",counter_ex_12,"")
else: 
    print ("La letra no se encuentra")


# 13-	Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


phrase_ex_13 = str(input("Ingrese la frase que quiera. Escriba, (salir) para terminar el proceso: "))
concatenated_phrase_ex_13 = phrase_ex_13


while phrase_ex_13 != "salir":
    print(concatenated_phrase_ex_13)
    phrase_ex_13 = str(input("Ingrese la frase que quiera. Escriba, (salir) para terminar el proceso: "))
    concatenated_phrase_ex_13 = concatenated_phrase_ex_13 + " "+ phrase_ex_13

print("Proceso Finalizado.")


# 14-	Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.


numbers_ex_14 = [int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))]
                      
for i_ex_14 in numbers_ex_14:
    if i_ex_14 % 2 == 0:
        print(i_ex_14, "es un número par")
    else:
        print(i_ex_14 , "es un numero impar")


# 15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.


number_ex_15 = int(input("Ingrese un número mayor a 0, entero: "))
i_ex_15 = 0

if number_ex_15 > 0:
    while i_ex_15 != number_ex_15 + 1:
        for i_ex_15 in range(1, number_ex_15 + 2,1):
            if number_ex_15 % i_ex_15  == 0:
                print(i_ex_15)
else: 
    print("¿Usted no tiene comprensión lectora?")


# 16-	Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

numbers_ex_16=int(input("Ingrese cuantos números desea ingresar: "))
counter_ex_16 = 0

for i_ex_16 in range(numbers_ex_16):
    i_ex_16 = float(input("Ingrese un número porfavor: "))
    if i_ex_16 < 0 :
        counter_ex_16+=1
    
if counter_ex_16 > 0:
    print("Usted ingresó ",counter_ex_16, "números negativos. ")
else:
    print("No hay números negativos.")


# 17-	Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).


phrase_ex_17 = str(input("Ingrese una frase: ")).lower()
a_counter_ex_17 = 0
e_counter_ex_17 = 0
i_counter_ex_17 = 0
o_counter_ex_17 = 0
u_counter_ex_17 = 0

for i_ex_17 in phrase_ex_17 :
    if i_ex_17 == "a":
        a_counter_ex_17 += 1
    elif i_ex_17 == "e":
        e_counter_ex_17 += 1
    elif i_ex_17 == "i":
        i_counter_ex_17 += 1
    elif i_ex_17 == "o":
        o_counter_ex_17 += 1
    elif i_ex_17 == "u":
        u_counter_ex_17 += 1

if a_counter_ex_17 >0: 
    print("A, aparece en la frase")

if e_counter_ex_17 >0: 
    print("E, aparece en la frase")

if i_counter_ex_17 >0:
    print ("I, aparece en la frase")

if o_counter_ex_17>0:
    print ("O, aparece en la frase")

if u_counter_ex_17>0:
    print ("U, aparece en la frase")


# 18-	Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…


fibbo_sequence_ex_18 = [0,1]
for i_ex_18 in range(2,11):
    next_number_ex_18 = fibbo_sequence_ex_18[-1] + fibbo_sequence_ex_18[-2]
    fibbo_sequence_ex_18.append(next_number_ex_18)

print(fibbo_sequence_ex_18)


# 19-	Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.


savings_goal_ex_19 = float(input("Su meta de ahorro: "))
savings_ex_19 = 0

while savings_ex_19 <= savings_goal_ex_19:
    incomes_ex_19= (float(input("Ingrese dinero: ")))
    if incomes_ex_19 > 0:
        savings_ex_19 = savings_ex_19 + incomes_ex_19
    else:
        print("Los Ingresos deben ser positivos.")
print("Objetivo alcanzado usted recaudó: ", savings_ex_19)


# 20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

i_ex_20 = None
counter_ex_20 = 0
while i_ex_20 != 0: 
    i_ex_20= float(input("Ingrese un númnero: "))
    counter_ex_20= counter_ex_20 + i_ex_20;

print("La suma de los número ingresados es de: ", counter_ex_20 )


# 21-	Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.


number_ex_21 = 1
largest_number = 0
while number_ex_21 != 0 :
    number_ex_21 = int(input("Ingrese un número entero positivo: "))
    if  number_ex_21 > largest_number:
        largest_number = number_ex_21
    
print("el número más grande ingresado: ", largest_number)


# 22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.


# Initialize a variable to count even numbers
even_numbers_ex_22 = 0

# Loop to ask for positive integers and calculate the sum of digits
while True:
    number_ex_22 = int(input("Ingresa un número positivo entero o (-1) para finalizar: "))
    
    # Check if it's time to exit the loop
    if number_ex_22 == -1:
        break
    
    # Check if the number is even
    if number_ex_22 % 2 == 0:
        even_numbers_ex_22 += 1
    
    # Calculate the sum of digits
    sum_of_digits_ex_22 = sum(int(digit) for digit in str(abs(number_ex_22)))
    
    # Print the sum of digits
    print("La suma de los dígitos de", number_ex_22, "es:", sum_of_digits_ex_22)

# Print the count of even numbers entered
print("Cantidad de números pares ingresados:", even_numbers_ex_22)


''' 
23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
    &
24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.'''
compra_23 = None
total_compra_ex_23 = 0
while compra_23 != 0: 
    compra_23= float(input("Ingrese El monto de la compra: "))
    if compra_23 >= 0:
        total_compra_ex_23= total_compra_ex_23 + compra_23;
    else: 
        print("Monto Negativo, vuelva a ingresar el monto: ")

if total_compra_ex_23 > 1000:
    descuento_ex_23 =float((total_compra_ex_23*0.10))
    total_compra_ex_23=total_compra_ex_23-descuento_ex_23
    print("El total con el 10% de descuento es de: ", total_compra_ex_23)
else:
    print("Total sin Descuento",total_compra_ex_23)

# 25-	Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.


import sys

number_ex_25 = int(input("Ingresa un número positivo entero: "))

if number_ex_25 == 0 :
    print("Facorial = 1" )
    sys.exit()

factorial_ex_25 = 1 

for i_ex_25 in range(1,number_ex_25 + 1):
    factorial_ex_25 *= i_ex_25
    

print (factorial_ex_25)


