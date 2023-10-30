operador = ""
class Calculadora:
  def __init__(self):
    self.operador = ""
    self.num1 = 0
    self.num2 = 0
  def suma(self, num1, num2):
    return num1 + num2
  def resta(self, num1, num2):
    return num1 - num2
  def division(self, num1, num2):
    return  num1 / num2
  def multiplicacion(self, num1, num2):
    return num1 * num2
  
calculadora = Calculadora()

