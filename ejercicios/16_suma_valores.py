'''
16.- Confeccionar una función que reciba entre 2 y 5 enteros.
La misma nos debe retornar la suma de dichos valores.
Debe tener tres parámetros por defecto.
'''

numeros = []

cuantos_numeros = int(input("Introduzca cuantos numeros quiere para el sumatorio: "))

while cuantos_numeros < 3:
  cuantos_numeros = int(input("Deben ser tres o más: "))

if cuantos_numeros >= 3:
  for iter in range(cuantos_numeros):
    numero = int(input("Introduce los números: "))
    numeros.append(numero)
    
def sumatorio(array_nums):
  suma = 0
  for iter in range(len(numeros)):
    suma += numeros[iter]
  return suma
  
print(sumatorio(cuantos_numeros))

##########################          ##################

num1, num2, num3 = 0, 0, 0

num1 = int(input("Introduce el primero numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercer numero: "))

def sumatorio(valor1, valor2, valor3):
  suma = 0
  suma = valor1 + valor2 + valor3
  return suma

print(sumatorio(num1, num2, num3))