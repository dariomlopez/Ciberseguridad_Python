import sqlite3
import tkinter as tkinter
# from tkinter import scrolledtext as st

class ModificarContacto(tkinter.Frame):
  def __init__(self, parentTab):
    super().__init__(parentTab)
    
    self.label_id = tkinter.Label(
      self, text="Introduce el id del contacto que quieres modificar: ")
    self.label_nombre = tkinter.Label(
      self, text="Introduce el nombre del contacto que quieres modificar: ")
    
    self.id = tkinter.IntVar()
    self.nombre = tkinter.StringVar()
    # self.telefono = tkinter.IntVar()
    # self.email = tkinter.StringVar()
    
    self.entry_id = tkinter.Entry(
      self, width=25, textvariable=self.id)
    self.entry_nombre = tkinter.Entry(
      self, width=25, textvariable=self.nombre)
    # self.entry_telf = tkinter.Entry \
    #   (self, width=25, textvariable=self.telefono)
    # self.entry_email = tkinter.Entry \
    #   (self, width=25, textvariable=self.email)
    
    self.label_id.pack()
    self.entry_id.pack()
    self.label_nombre.pack()
    self.entry_nombre.pack()
    # self.label_telf.pack()
    # self.entry_telf.pack()
    # self.label_email.pack()
    # self.entry_email.pack()
    self.label1 = tkinter.Label(self, text="Nuevos datos")
    self.label1.pack()
    self.label_nombre_mod = tkinter.Label(
      self, text="Introduce el nuevo nombre")
    self.label_telf_mod = tkinter.Label(
    self, text="Introduce el nuevo teléfono")
    self.label_email_mod = tkinter.Label(self, text="Introduce un nuevo email")
    
    self.nombre_mod = tkinter.StringVar()
    self.telefono_mod = tkinter.IntVar()
    self.email_mod = tkinter.StringVar()
    
    self.entry_nombre_mod = tkinter.Entry(
      self, width=25, textvariable=self.nombre)
    self.entry_telf_mod = tkinter.Entry(self, width=25, textvariable=self.telefono_mod)
    self.entry_email_mod = tkinter.Entry(self, width=25, textvariable=self.email_mod)
    
    self.label_nombre_mod.pack()
    self.entry_nombre_mod.pack()
    self.label_telf_mod.pack()
    self.entry_telf_mod.pack()
    self.label_email_mod.pack()
    self.entry_email_mod.pack()
    
    self.botonMod = tkinter.Button(self, text="Modificar", command=self.modificarContacto)
    self.botonMod.pack()
    # self.scrolledtext = st.ScrolledText(self)
    # self.scrolledtext.pack()
  
  def modificarContacto(self):
    id = self.entry_id.get()
    nombre = self.entry_nombre.get()
    nombre_mod = self.entry_nombre_mod.get()
    telf_mod = self.entry_telf_mod.get()
    email_mod = self.entry_email_mod.get()
    
    conn = sqlite3.connect("C:/Users/junky/Desktop/Ciberseguridad y hacking/Python/ejercicios_tkinter/ejercicio41/agendaDB.db")
    cursor = conn.cursor()
    try:
      query= f"""
          update agenda
          set nombre = ?,
            telefono= ?,
            email = ?
          where id= ?
          or nombre = ?
        """
      params = (id, nombre, nombre_mod, telf_mod, email_mod)
      cursor.execute(query, params)
      conn.commit()
      
      # cursor.execute("SELECT * FROM agenda")
      # datos_mod = cursor.fetchall()
      #
      # for idx, contact in enumerate(datos_mod):
      #     contact_mod = (f"ID: {contact[0]},\n"
      #                     f"Nombre: {contact[1]},\n"
      #                     f"Teléfono: {contact[2]},\n"
      #                     f"Email: {contact[3]}\n")
      #     self.scrolledtext.insert(tkinter.END, contact_mod)
    finally:
      conn.close()