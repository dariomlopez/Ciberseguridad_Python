import tkinter as tkinter
import sqlite3

class BorrarContacto(tkinter.Frame):
  def __init__(self, parentTab):
    super().__init__(parentTab)
    
    self.label_id = tkinter.Label(self, text="Introduce el id del contacto a eliminar")
    self.label_nombre = tkinter.Label(
      self, text="Introduce el nombre del contacto que quieres eliminar: ")
    
    self.id = tkinter.IntVar()
    self.nombre = tkinter.StringVar()
    
    self.entry_id = tkinter.Entry(
      self, width=25, textvariable=self.id)
    self.entry_nombre = tkinter.Entry(
      self, width=25, textvariable=self.nombre)
    
    self.label_id.pack()
    self.entry_id.pack()
    self.label_nombre.pack()
    self.entry_nombre.pack()
   
    
    self.botonBorrar = tkinter.Button(self, text="Borrar", command=self.eliminarContacto)
    self.botonBorrar.pack()
  
  def eliminarContacto(self):
    id_cod = self.entry_id.get()
    nombre = self.entry_nombre.get()
    
    conn = sqlite3.connect("C:/Users/junky/Desktop/Ciberseguridad y hacking/Python/ejercicios_tkinter/ejercicio41/agendaDB.db")
    cursor = conn.cursor()
    try:
      query = f"""
          delete from agenda
          where id = ?,
            nombre = ?
        """
      
      cursor.execute(query, (id_cod, nombre))
      conn.commit()
      
      # cursor.execute("SELECT * FROM agenda")
      # datos_mod = cursor.fetchall()
      #
      # for idx, contact in enumerate(datos_mod):
      #   contact_mod = (f"ID: {contact[0]},\n"
      #                  f"Nombre: {contact[1]},\n"
      #                  f"Teléfono: {contact[2]},\n"
      #                  f"Email: {contact[3]}\n")
      #   self.scrolledtext.insert(tkinter.END, contact_mod)
    finally:
      conn.close()