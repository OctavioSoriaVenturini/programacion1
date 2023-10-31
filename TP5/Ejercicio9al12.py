# EJ N9
# Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
def login(user1, passw):
    if user1 == "usuario1" and passw == "asdasd":
        return True
    else:
        return False

iter = 0
while True:
    iter +=1
    user1 = input("Ingrese su usuario ")
    passw = input("Ingrese su contraseña ")
    if login(user1, passw):
        print(f"Correcto, cantidad de intentos {iter} ")
        break
    else:
        print(f"Incorrecto, intento N{iter} ")

# EJ N10
# Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los precios y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra.
def aplicar_descuentos(cart, sale):
    final_price = 0
    x = 0
    for prod2 in cart:
        
        sale1 = cart[x] * (sale / 100)
        price_with_sale = prod2 - sale1
        final_price += price_with_sale
        x=+1
    return final_price

# Ejemplo de carrito de compra
shopping_cart = []
while True:
    prod = int(input("Ingrese el precio del producto(si desea salir ingrese 0) "))
    if prod == 0:
        break
    shopping_cart.append(prod)
    
sale = 20
total_price = aplicar_descuentos(shopping_cart, sale)
print(f"Precio total con descuentos: ${total_price:.2f}")

# EJ N11 Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.

def aplicar_funcion_a_lista(function, list):
    results = []
    for element in list:
        results = function(element)
        results.append(results)
    return results

# Ejemplo de uso:
def cuadrado(x):
    return x ** 2

# creamos la parte principal del ejercicio
original_list = [1, 2, 3, 4, 5]
result = aplicar_funcion_a_lista(cuadrado, original_list)
print(result)  # Salida: [1, 4, 9, 16, 25]

# EJ N12 Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
def contar_longitud_palabras(phrase):
    words = phrase.split()  # Dividir la frase en palabras
    result = {}
    for word in words:
        result[word] = len(word)
    return result

# parte principal en la cual llamamos a la funcion contar_longitud_palabras
phrase = input("Ingrese una frase")
result = contar_longitud_palabras(phrase)
print(result)  