'''
Crear una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.
'''

class Agenda:
  
  def __init__(self, nombre, telefono, email):
    self.nombre = nombre
    self.telefono = telefono
    self.email = email
    self.lista_agenda = []
    
  def iniciar_agenda(self):
    nombre = str(input("Introduce el nombre: "))
    telefono = int(input("Introduce el teléfono: "))
    email = str(input("Introduce un email"))
    contacto = Agenda(nombre, telefono, email)
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
    nombre = str(input("Ingresa el nombre del contacto a modificar: "))
    for contacto in self.lista_agenda:
      if contacto.nombre.lower() == nombre.lower():
        nuevo_nombre = str(input("Introduce el nuevo nombre"))
        nuevo_tlf = int(input("Introduce el nuevo teléfono"))
        nuevo_email = str(input("Introduce el nuevo email"))
        contacto.nombre = nuevo_nombre
        contacto.telefono = nuevo_tlf
        contacto.email = nuevo_email
        print("Contacto modificado con exito: ")
        print(f"Nombre: {contacto.nuevo_nombre}, Teléfono: {contacto.nuevo_tlf}, Email:"
              f" {contacto.nuevo_email}")
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
      
  def listado(self, lista_agenda):
    print(lista_agenda)
  

agenda1 = Agenda("Juan", 4567464, "juan@test.es")
agenda1.cargar_contacto()