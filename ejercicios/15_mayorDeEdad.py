'''
15.- Confeccionar una función que reciba una
serie de edades y me retorne la cantidad que son
mayores o iguales a 18 (como mínimo se envía un entero a la función)
'''

def edad_mas_18():
  edades = []
  contador, contador18 = 0, 0
  
  cuantas_edades = int(input("Cuantas edades quieres introducir"))
  
  for iter in range(cuantas_edades):
    edad = int(input("Introduce una edad: "))
    edades.append(edad)
    
  for edad in edades:
    if edad >= 18:
      contador18 += 1
    else:
      contador += 1
    
  print(f"Menores de 18 años: {contador} Mayores de 18 años: {contador18}")
  
edad_mas_18()

########################################
edades = []

cuantas_edades = int(input("Cuántas edades quieres introducir: "))

for iter in range(cuantas_edades):
  edad = int(input("Introduce una edad: "))
  edades.append(edad)
  
def mayormenor(array_edades):
  contador, contador18 = 0, 0
  for edad in edades:
    if edad >= 18:
      contador18 += 1
    else:
      contador += 1
  print(f"Menores de 18 años: {contador} Mayores de 18 años: {contador18}")

mayormenor(edades)