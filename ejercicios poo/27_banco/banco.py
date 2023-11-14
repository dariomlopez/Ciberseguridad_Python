'''
Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. También el banco requiere que al final del día calcule la cantidad de dinero que hay depositado.
'''

from cliente import *

class Banco:
  def __init__(self):
    self.cliente1 = Cliente("Ángela")
    self.cliente2 = Cliente("Jóse")
    self.cliente3 = Cliente("Monica")
    
  def operacion(self):
    self.cliente1.depositar(3000)
    self.cliente1.depositar(500)
    self.cliente2.depositar(1000)
    self.cliente2.depositar(1100)
    self.cliente3.depositar(500)
    self.cliente3.depositar(650)
    self.cliente2.retirar(100)
    self.cliente1.retirar(700)
    
  def depositos(self):
    total = (self.cliente1.cantidad_total() + self.cliente2.cantidad_total() +
             self.cliente3.cantidad_total())
    print(f"Total de dinero del banco al final del día: {total}")
    
    self.cliente1.imprimir()
    self.cliente2.imprimir()
    self.cliente3.imprimir()
    
banco1 = Banco()
print(banco1.operacion())
print(banco1.depositos())