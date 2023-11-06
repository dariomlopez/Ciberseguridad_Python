'''
13.- Confeccionar una función que:
- calcule la superficie de un rectángulo y la retorne,
la función recibe como parámetros los valores de dos de sus lados:
                    def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos
y luego mostrar cual de los dos tiene una superficie mayor.
'''

"""Pedimos la introducción de datos por teclado"""
altura1 = float(input("Introduce la altura del primer rectangulo: "))
ancho1 = float(input("Introduce la anchura del primer rectangulo: "))
altura2 = float(input("Introduce la altura del segundo rectangulo: "))
ancho2 = float(input("Introduce la anchura del segundo rectangulo: "))

"""Definimos la función"""
def superficie_rectangulo(altura, ancho):
  superficie = altura * ancho
  return superficie

"""Llamada a la función con los argumentos que nos ha pasado el usuario"""
rect1 = superficie_rectangulo(altura1, ancho1)
rect2 = superficie_rectangulo(altura2, ancho2)

"""Imprimimos la superficie"""
print(f"Superficie del primer rectangulo con altura {altura1} y ancho {ancho1}: {rect1}")
print(f"Superficie del segundo rectangulo con altura {altura2} y ancho {ancho2}: {rect2}")

if rect1 > rect2:
  print("El primer rectangulo más grande")
else:
  print("El segundo rectangulo es más grande")
  
#########################        ##########             ################

