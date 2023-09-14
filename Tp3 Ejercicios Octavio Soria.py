# 4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.


number_ex_4= int(input("Ingrese un número entero positivo: "))

for i_ex_4 in range (number_ex_4, 0 ,-1):
    print(i_ex_4, end=", ")
print(0)

# 8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.


number_ex_8= int(input("Ingrese un número entero positivo: "))

for i_ex_8 in range(1, number_ex_8 + 1):
    for j_ex_8 in range(i_ex_8, 0, -1):
        print(j_ex_8, end="")
    print()

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


# 20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

i_ex_20 = None
counter_ex_20 = 0
while i_ex_20 != 0: 
    i_ex_20= float(input("Ingrese un númnero: "))
    counter_ex_20= counter_ex_20 + i_ex_20;

print("La suma de los número ingresados es de: ", counter_ex_20 )


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
