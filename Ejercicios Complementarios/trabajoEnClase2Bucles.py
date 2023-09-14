'''Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6
integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”.
La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que
deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un
método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del
mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares.
Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales.
Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se
correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el
mismo corrimiento.
Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a
comenzar desde la letra “a”.
Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto
español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una
vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.
'''
# abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

mensajes = []  # Creamos una lista para almacenar los mensajes
desplazar= int(input("Ingresar el valor de desplazamiento: "))
for i in range(5):
    mensaje = input("Ingresa un mensaje: ")
    mensajes.append(mensaje)  # Agregamos el mensaje a la lista

def encriptar(mensaje, desplazar):
    mensaje_encriptado=""
    for letra in mensaje:
        if letra.isalpha():
            valor_letra= ord(letra)
            valor_letra_nuevo=(valor_letra - ord('a')+desplazar) % 26 + ord('a')
            letra_encriptada=chr(valor_letra_nuevo)
            mensaje_encriptado= mensaje_encriptado + letra_encriptada # mensaje_encriptado += letra_encriptada
            
        else:
            mensaje_encriptado = mensaje_encriptado + letra
    return mensaje_encriptado

for mensaje in mensajes:
    mensaje_encriptado = encriptar(mensaje,desplazar)
    print ("Mensaje original: ", mensaje)
    print("Palabra encriptada: ", mensaje_encriptado)
    print()

#EJERCICIO 2
'''Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.'''
numeros = []
contador_pares = 0
contador_impares = 0

while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break  # Sale del bucle cuando se ingresa 0
    numeros.append(numero)  # Agrega el número a la lista numeros

for numero in numeros:
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

print("Se han ingresado:", contador_pares, "números pares")
print("Se han ingresado:", contador_impares, "números impares")
