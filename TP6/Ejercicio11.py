diccionario_divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa = input("Ingresa una divisa: ")

if divisa in diccionario_divisas:
    print(f"El símbolo de la divisa {divisa} es: {diccionario_divisas[divisa]}")
else:
    print("La divisa no está en el diccionario.")
