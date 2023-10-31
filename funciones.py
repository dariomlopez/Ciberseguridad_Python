def sumar(*args):
  total = 0
  for numero in args:
    total += numero
  return total

#argumentos = (5, 10, 15, 35, 50)

suma = sumar(5, 10, 15, 35, 50)

print(suma)