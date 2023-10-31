def longitud_ultima_palabra():
  texto = input("Ingrese el texto: ")
  
  palabras = texto.split()
  ultima_palabra = palabras[-1]

  longitud = len(ultima_palabra)

  print(f"La longitud de la última palabra es: {longitud}")

longitud_ultima_palabra()