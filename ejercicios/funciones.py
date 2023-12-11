def sumar(*args):
  total = 0
  for numero in args:
    total += numero
  return total

#argumentos = (5, 10, 15, 35, 50)

suma = sumar(5, 10, 15, 35, 50)

print(suma)

'''
#por valor
n = 10
def doblarValor(numero):
numero *= 2
print(numero,"está dentro de la función pasar por valor")

doblarValor(n)
print(n)

#por referencia
ns = [10, 50, 25]
def doblarValor(numeros):
for i, n in enumerate(numeros):
numeros[i] *= 2
print(numeros[i],"está dentro de la función pasar por referencia")

doblarValor(ns)
print(ns)

#por valor, pero modificando la variable original
n = 10
def doblarValor(numero):
return numero * 2#al retornar, lo que hacemos es modificar la "copia original" de la variable

doblarValor(n)
print(n)
'''