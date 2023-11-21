'''
Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar los datos cargados.

- Imprimir un mensaje si es mayor de edad (edad>=18)
'''

class Datos:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    # nombre = str(input("Introduce un nombre"))
    # edad = int(input("introduce una edad"))
  
  def imprimir(self):
    print(f"Nombre: {self.nombre} - {self.edad}")
  
  def mayor18(self):
    if self.edad > 18:
      print(f"{self.nombre} es mayor de edad")
    else:
      print(f"{self.nombre} es menor de edad")
      

persona1 = Datos("Pepe", 14)
persona2 = Datos("Ramón", 41)
persona3 = Datos("Iñaki", 22)

persona1.imprimir(), persona1.mayor18()
persona2.imprimir(), persona2.mayor18()
persona3.imprimir(), persona3.mayor18()
