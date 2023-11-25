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
#from agenda import Agenda

# agenda = Agenda()
# agenda.menu()

class Main(ttk.Frame):
  def __init__(self):
    self.ventana = tkinter.Tk()
    self.ventana.title("Agenda")
    self.ventana.geometry("400x400")
    
    self.label_nombre = tkinter.Label(self.ventana, text="Introduce un nombre: ")
    self.label_telf = tkinter.Label(self.ventana, text="Introduce el teléfono: ")
    self.label_email = tkinter.Label(self.ventana, text="Introduce el email: ")
    
    self.label_nombre.grid(column=0, row=0)
    self.label_telf.grid(column=0, row=1)
    self.label_email.grid(column=0, row=2)
    
    self.nombre = tkinter.StringVar()
    self.telefono = tkinter.IntVar()
    self.email = tkinter.StringVar()
    
    self.entry_nombre = tkinter.Entry(self.ventana, width=25, textvariable=self.nombre)
    self.entry_telf = tkinter.Entry(self.ventana, width=25, textvariable=self.telefono)
    self.entry_email = tkinter.Entry(self.ventana, width=25, textvariable=self.email)
    
    self.entry_nombre.grid(column=1, row=0)
    self.entry_telf.grid(column=1, row=1)
    self.entry_email.grid(column=1, row=2)
    
    self.ventana.mainloop()
    
aplicacion = Main()