'''
Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. También el banco requiere que al final del día calcule la cantidad de dinero que hay depositado.
'''

class Cliente:
  def __init__(self, nombre):
    self.nombre = nombre
    self.cantidad = 0
    
  def depositar(self, cantidad):
    self.cantidad += cantidad
    
  def retirar(self, cantidad):
    self.cantidad -= cantidad
    
  def cantidad_total(self):
    return self.cantidad
  
  def imprimir(self):
    print(f"{self.nombre} tiene una cantidad de {self.cantidad}")
  