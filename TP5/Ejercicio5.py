# Función para calcular la temperatura media
def calcular_temp_media(temp_max, temp_min):
  return (temp_max + temp_min) / 2

# Programa principal
dias = int(input("¿Cuántos días va a introducir? "))

for i in range(dias):
  temp_max = float(input(f"Temperatura máxima día {i+1}: "))
  temp_min = float(input(f"Temperatura mínima día {i+1}: "))

  media = calcular_temp_media(temp_max, temp_min)
  
  print(f"Temperatura media día {i+1}: {media} °C")

  