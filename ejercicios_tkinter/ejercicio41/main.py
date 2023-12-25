'''
Basándonos en el ejercio23.py implementar con tkinter
(Crear una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.) implementar un programa ya utilizando la parte gráfica..... ¡¡Adelante mis valientes!!
'''

import tkinter as tkinter
from tkinter import ttk
from agregarContacto import AgregarContacto
from listaContactos import ListaContactos
from consultaContacto import ConsultarContacto
from modificarContacto import ModificarContacto
from borrarContacto import BorrarContacto
from finalizar import Finalizar
#from agenda import Agenda

# agenda = Agenda()
# agenda.menu()

class Main(ttk.Frame):
  def __init__(self, ventana):
    super().__init__(ventana)
    
    ventana.title("Agenda")
    ventana.geometry("900x600")
    
    self.parentTab = ttk.Notebook(self)
    
    self.tabAgregar = AgregarContacto(self.parentTab)
    self.tabListado = ListaContactos(self.parentTab)
    self.tabConsulta = ConsultarContacto(self.parentTab)
    self.tabModificar = ModificarContacto(self.parentTab)
    self.tabBorrar = BorrarContacto(self.parentTab)
    self.tabFinalizar = Finalizar(self.parentTab)
    
    self.parentTab.add(self.tabAgregar, text="Agregar contacto", padding=100)
    self.parentTab.add(self.tabListado, text="Listado completo de contactos", padding=10)
    self.parentTab.add(self.tabConsulta, text="Buscar contacto", padding=10)
    self.parentTab.add(self.tabModificar, text="Modificar contacto", padding=100)
    self.parentTab.add(self.tabBorrar, text="Borrar contacto", padding=100)
    self.parentTab.add(self.tabFinalizar, text="Salir de la aplicación", padding=100)
    
    self.parentTab.pack(padx=0, pady=0)
    self.pack()

    

ventana = tkinter.Tk()
aplicacion = Main(ventana)
aplicacion.mainloop()