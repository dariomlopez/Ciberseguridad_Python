'''
Crear una clase que administre una agenda personal.
- Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.
'''

class Contacto():
  def __init__(self, nombre, telefono, email):
    self.nombre = nombre
    self.telefono = telefono
    self.email = email

class Agenda:
  
  def __init__(self):
    self.lista_agenda = []
    
  def iniciar_agenda(self):
    nombre = str(input("Introduce el nombre: "))
    telefono = int(input("Introduce el teléfono: "))
    email = str(input("Introduce un email: "))
    contacto = Contacto(nombre, telefono, email)
    self.lista_agenda.append(contacto)
  
  def cargar_lista(self):
    if not self.lista_agenda:
      print("Agenda vacía")
    else:
      for contacto in self.lista_agenda:
        print(
        f"Nombre - Teléfono - Email\n"
        f"{contacto.nombre} - {contacto.telefono} - {contacto.email}")
  
  def buscar(self):
    nombre = str(input("Ingresa el nombre del contacto: "))
    for contacto in self.lista_agenda:
      if contacto.nombre.lower() == nombre.lower():
        print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
      else:
        print("Contacto no encontrado")
        
  def modificar(self):
    nombre = str(input("Ingresa el nombre del contacto que quieres modificar: "))
    for contacto in self.lista_agenda:
      if contacto.nombre.lower() == nombre.lower():
        nombre = str(input("Introduce el nuevo nombre"))
        telefono = int(input("Introduce el nuevo teléfono"))
        email = str(input("Introduce el nuevo email"))
        contacto.nombre = nombre
        contacto.telefono = telefono
        contacto.email = email
        print("Contacto modificado con exito: ")
        print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email:"
              f" {contacto.email}")
      else:
        print("Contacto no encontrado")
        
  def menu(self):
    opcion = 0
    while opcion != 5:
      print(
      """
      Introduce la opción:
      1 - Carga de un contacto en la agenda.
      2 - Listado completo de la agenda.
      3 - Consulta ingresando el nombre de la persona.
      4 - Modificación de su teléfono y mail.
      5 - Finalizar programa
      """)
      opcion = int(input("Opción: "))
      if opcion == 1:
        self.iniciar_agenda()
      elif opcion == 2:
        self.cargar_lista()
      elif opcion == 3:
        self.buscar()
      elif opcion == 4:
        self.modificar()
      elif opcion == 5:
        print("Cerrando aplicación...Adios")
        break
      else:
        print("Opción invalida. Intentalo de nuevo")
        self.menu()

agenda1 = Agenda()
agenda1.menu()