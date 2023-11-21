'''
Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento.
'''

class Persona:
  
  def __init__(self, num_documento, nombre):
    self.num_documento = num_documento
    self.nombre = nombre
  
class Diccionario:
  def __init__(self):
    self.diccionaro_personas = {}
    
  def agregar(self):
    for i in range(4):
      num_documento = int(input("Introduce el número de documento: "))
      nombre = str(input("Introduce el nombre de la persona: "))
      persona1 = Persona(num_documento, nombre)
      self.diccionaro_personas[num_documento] = nombre
    
  def mostrar_diccionario(self):
    if not self.diccionaro_personas:
      print("No hay datos para mostrar.")
    else:
      for documento, nombre in (self.diccionaro_personas.items()):
        print(f"Documento: {documento} - Nombre {nombre}")
        
  def buscar_nombre(self):
    documento = int(input("Introduzca el número de documento de la persona: "))
    if not self.diccionaro_personas:
      print("No hay datos para mostrar.")
    else:
      if documento in self.diccionaro_personas.keys():
        for num_documento, nombre in self.diccionaro_personas.items():
          if num_documento == documento:
            print(f"Nombre: {nombre}")
