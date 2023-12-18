import sqlite3
import tkinter as tkinter
from tkinter import scrolledtext as st

class ModificarContacto(tkinter.Frame):
  def __init__(self, parentTab):
    super().__init__(parentTab)
    # tabAgregar = ttk.Label(parentTab, text="Agregar contacto")
    self.label_nombre = tkinter.Label(
      self, text="Introduce el nombre del contacto que quieres "
                 "modificar: ")
    self.label_telf = tkinter.Label(
      self, text="Teléfono que quieres buscar: ")
    self.label_email = tkinter.Label \
      (self, text="Email que quieres buscar: ")
    
    self.nombre = tkinter.StringVar()
    self.telefono = tkinter.IntVar()
    self.email = tkinter.StringVar()
    
    self.entry_nombre = tkinter.Entry(
      self, width=25, textvariable=self.nombre)
    self.entry_telf = tkinter.Entry \
      (self, width=25, textvariable=self.telefono)
    self.entry_email = tkinter.Entry \
      (self, width=25, textvariable=self.email)
    
    self.label_nombre.pack()
    self.entry_nombre.pack()
    self.label_telf.pack()
    self.entry_telf.pack()
    self.label_email.pack()
    self.entry_email.pack()
    
    self.botonMod = tkinter.Button(self, text="Modificar", command=self.modificarContacto)
    self.botonMod.pack()
    self.scrolledtext = st.ScrolledText(self)
    self.scrolledtext.pack()
  
  def modificarContacto(self):
    nombre = self.entry_nombre.get()
    telf = self.entry_telf.get()
    email = self.entry_email.get()
    nombre_mod = self.entry_nombre.get()
    telf_mod = self.entry_telf.get()
    email_mod = self.entry_email.get()
    
    conn = sqlite3.connect("C:/Users/junky/Desktop/Ciberseguridad y hacking/Python/ejercicios_tkinter/ejercicio41/agendaDB.db")
    cursor = conn.cursor()
    try:
      query= f"""
          update agenda
          set nombre = ?,
            telefono= ?,
            email = ?
          where nombre = ?
            or telefono= ?
            or email = ?
        """
    
      cursor.execute(query, (nombre_mod, telf_mod, email_mod, nombre, telf, email))
      conn.commit()
      
      cursor.execute("SELECT * FROM agenda")
      datos_mod = cursor.fetchall()
      
      for idx, contact in enumerate(datos_mod):
          contact_mod = (f"ID: {contact[0]},\n"
                          f"Nombre: {contact[1]},\n"
                          f"Teléfono: {contact[2]},\n"
                          f"Email: {contact[3]}\n")
          self.scrolledtext.insert(tkinter.END, contact_mod)
    finally:
      conn.close()