def es_multiplo(num1, num2):
  if num1 % num2 == 0:
    return True  
  else: 
    return False

print("Introduzca dos números enteros:")

numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

if es_multiplo(numero1, numero2):
  print(f"{numero1} es múltiplo de {numero2}")
else:
  print(f"{numero1} NO es múltiplo de {numero2}")