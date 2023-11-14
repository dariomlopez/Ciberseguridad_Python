'''
28- Definir:
-una clase Cliente que almacene un código de cliente y un nombre.
En la clase Cliente:
 -definir una variable de clase de tipo lista que almacene todos los clientes que
 tienen suspendidas sus cuentas corrientes.
 - Imprimir por pantalla todos los datos de clientes y
 - el estado que se encuentra su cuenta corriente.
'''

class Cliente:
  lista_cuentas = []
  
  def __init__(self, codigo_cliente, nombre):
    self.codigo = codigo_cliente
    self.nombre = nombre
    
  def imprimir(self):
    print("###############")
    print(f"Cuenta a nombre de {self.nombre} -- Codigo: {self.codigo} "
          f"\nEstado: ")
    self.estado()
    
  def estado(self):
    if self.codigo in Cliente.lista_cuentas:
      print("Cuenta suspendida")
    else:
      print("Cuenta no suspendida")
    print("###############")
      
  def suspender(self):
    Cliente.lista_cuentas.append(self.codigo)
      
cliente1 = Cliente(1, "Pepe")
cliente2 = Cliente(2, "Juan")
cliente3 = Cliente(3, "Josefa")
cliente4 = Cliente(4, "Juana")

cliente2.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

#print(Cliente.lista_cuentas)