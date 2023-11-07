'''
16.- Confeccionar una función que reciba entre 2 y 5 enteros.
La misma nos debe retornar la suma de dichos valores.
Debe tener tres parámetros por defecto.
'''

'''numeros = []

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
'''
##########################          ##################

def sumatorio(valor1 = 0, valor2 = 0, valor3 = 0, *valores):
  suma = valor1 + valor2 + valor3
  for valor in range(len(valores)):
    suma += valores[valor]
  return suma

print(sumatorio(30, 22, 11, 40))