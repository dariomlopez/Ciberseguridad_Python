import tkinter as tkinter
import sqlite3

class AgregarContacto(tkinter.Frame):
  def __init__(self, parentTab):
    super().__init__(parentTab)
    
    self.label_nombre = tkinter.Label \
      (self, text="Introduce un nombre: ")
    self.label_telf = tkinter.Label \
      (self, text="Introduce el teléfono: ")
    self.label_email = tkinter.Label \
      (self, text="Introduce el email: ")
    
    self.label_nombre.grid(column=0, row=0)
    self.label_telf.grid(column=0, row=1)
    self.label_email.grid(column=0, row=2)
    
    # tipo de datos de las variables
    self.tipo_nombre = tkinter.StringVar()
    self.tipo_telefono = tkinter.IntVar()
    self.tipo_email = tkinter.StringVar()
    
    #  campos de entrada
    self.entry_nombre = tkinter.Entry \
      (self, width=25, textvariable=self.tipo_nombre)
    self.entry_telf = tkinter.Entry \
      (self, width=25, textvariable=self.tipo_telefono)
    self.entry_email = tkinter.Entry \
      (self, width=25, textvariable=self.tipo_email)
    
    self.entry_nombre.grid(column=1, row=0)
    self.entry_telf.grid(column=1, row=1)
    self.entry_email.grid(column=1, row=2)
    
    boton_guardar = tkinter.Button(self, text="Guardar",
                                   command=self.guardarContacto)
    boton_guardar.grid(column=1, row=3)
    
  def guardarContacto(self):
      nombre = self.entry_nombre.get()
      telefono = self.entry_telf.get()
      email = self.entry_email.get()
      
      conn = sqlite3.connect("C:/Users/junky/Desktop/Ciberseguridad y "
                             "hacking/Python/ejercicios_tkinter/ejercicio41/agendaDB.db")
      cursor = conn.cursor()
      
      try:
        cursor.execute("""
        drop table if exists agenda
        """)
        cursor.execute("""
        create table if not exists agenda (
          id integer primary key autoincrement,
          nombre text,
          telefono integer,
          email text
        )
        """)
        cursor.execute("""insert into agenda (nombre, telefono, email)
        values (?,?,?)""", (nombre, telefono,email))
        
        conn.commit()
    
      except:
        pass
      
      finally:
        conn.close()