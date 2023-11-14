'''26.- Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo.
Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.'''


# MAIN CLASS

class Cuenta:
  def __init__(self, titular, cantidad):
    self.titular = titular
    self.cantidad = cantidad
  
  def imprimir(self):
    print(f"{self.titular} tiene {self.cantidad}€ en su cuenta")


# Child Class

class CajaAhorro(Cuenta):
  def __init__(self, titular, cantidad):
    super().__init__(titular, cantidad)
  
  def imprimir(self):
    print("### Cuenta Caja de ahorros ###")
    super().imprimir()


class PlazoFijo(Cuenta):
  def __init__(self, titular, cantidad, plazo, interes):
    super().__init__(titular, cantidad)
    self.plazo = plazo
    self.interes = interes
  
  def imprimir(self):
    print("### Cuenta Plazo Fijo ###")
    super().imprimir()
    print(f"Día de plazo: {self.plazo} - Interés: {self.interes}")
    self.ganancia()
  
  def ganancia(self):
    interes = self.cantidad * self.interes / 100
    print(f"Importe del interés: {interes}")