import re

dni = input("Por favor ingrese su número de DNI: ")

patron = re.compile(r'\d{7,8}')
es_valido = patron.match(dni)

if es_valido:
  print("DNI válido")
else:
  print("DNI inválido")