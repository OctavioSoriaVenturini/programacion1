import re

# Expresión regular para validar el DNI 
patron_dni = re.compile(r'\d{7,8}')  

# Solicitar datos al usuario hasta que ingrese nombre vacío
print("Ingrese los datos de los socios (deje el nombre vacío para terminar)")
while True:
  nombre = input("Nombre: ")
  if nombre == "" :
    break

  nombre2 = input("Segundo nombre: ")
  apellido1 = input("apellido: ")
  
  # Validar DNI con expresión regular
  while True:
    dni = input("DNI: ")
    if patron_dni.match(dni):
      break
    else:
      print("DNI inválido. Debe tener 7 u 8 dígitos.")

  # Dividir el nombre ingresado y obtener apellido   
  nombres = apellido1.split(",") 
  apellido = nombres[-1]

  # Generar ID con formato solicitado
  id = nombres[0] + str(len(apellido)) + dni[:3]  

  # Mostrar ID generado
  print(f"ID generado: {id}\n")   
  print(nombre,nombre2,apellido1,dni)
#...Código anterior

# Mensaje de fin del programa  
print("Programa finalizado")
