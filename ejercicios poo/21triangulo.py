'''
Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos:
- inicializar los atributos,
- imprimir el valor del lado mayor
- método que muestre si es equilátero o no.
 nombre de la clase: Triangulo.
'''

class Triangulo:
  def __init__(self):
    lado1 = float(input("Introduzca el primer lado: "))
    lado2 = float(input("Introduzca el segundo lado: "))
    lado3 = float(input("Introduzca el tercer lado: "))
    self.lado1 = lado1
    self.lado2 = lado2
    self.lado3 = lado3
  
  def lado_mayor(self):
    if self.lado1 > self.lado2 and self.lado1 > self.lado3:
      print(f"El lado mayor es {self.lado1}")
    elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
      print(f"El lado mayor es {self.lado1}")
    else:
      print(f"El lado mayor es {self.lado3}")
  
  def es_equilatero(self):
    if (self.lado1 == self.lado2 and self.lado1 == self.lado3) and (self.lado2 == self.lado1 and self.lado2 == self.lado3):
      print(f"El triangulo es equilatero")
    else:
      print(f"El triangulo no es equilatero")
  
triangulo1 = Triangulo()
triangulo1.lado_mayor()
triangulo1.es_equilatero()