# EJ N 12 12.	Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje ‘<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>’.
# Crear un diccionario vacío para almacenar la información del usuario
user = {}

# Pedir al usuario que ingrese su nombre, edad, dirección y teléfono
user['nombre'] = input("Por favor, ingresa tu nombre: ")
user['edad'] = input("Ingresa tu edad: ")
user['dirección'] = input("Ingresa tu dirección: ")
user['teléfono'] = input("Ingresa tu número de teléfono: ")

# Mostrar la información almacenada en el diccionario
mensaje = f"{user['nombre']} tiene {user['edad']} años, vive en {user['dirección']} y su número de teléfono es {user['teléfono']}."
print(mensaje)

# EJ N13 Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Crear un diccionario con los precios de las frutas
kart = {
    "manzana": 1.5,
    "banana": 0.5,
    "naranja": 1.0,
    "uva": 2.0,
    "pera": 1.2
}

# Solicitar al usuario que ingrese una fruta
iter = 0
while True:
    if iter == 0:
        print("")
    else:
        answ = input("desea salir(S/N) ").upper()
        if answ == "S":
            break
        
    fruit = input("Ingresa el nombre de la fruta: ").lower()  

    if fruit in kart:
        try:
        
            kilos = float(input(f"Ingresa la cantidad de kilos de {fruit}: "))

            total_price = kart[fruit] * kilos

            print(f"El precio de {kilos} kilos de {fruit} es: ${total_price}")
        except ValueError:
            print("Ingresa una cantidad válida de kilos.")
    else:
        print("La fruta ingresada no está en la lista de precios.")