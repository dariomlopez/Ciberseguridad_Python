import tkinter as tkinter
import sqlite3
from tkinter import scrolledtext as st


class ListaContactos(tkinter.Frame):
  def __init__(self, parentTab):
    super().__init__(parentTab)
    self.botonListar = tkinter.Button(self, text="Agenda completa", command=self.agendaCompleta)
    self.botonListar.pack()
    self.scrolledtext = st.ScrolledText(self)
    self.scrolledtext.pack()
    
  def agendaCompleta(self):
    conn = sqlite3.connect("C:/Users/junky/Desktop/Ciberseguridad y hacking/Python/ejercicios_tkinter/ejercicio41/agendaDB.db")
    
    try:
      cursor = conn.cursor()
      cursor.execute("""
        select id, nombre, telefono, email from agenda
      """)
      
      contactos = cursor.fetchall()
      self.scrolledtext.delete("1.0", tkinter.END)
      
      for idx, contact in enumerate(contactos):
        contact_info = (f"ID: {contact[0]},\n"
                        f"Nombre: {contact[1]},\n"
                        f"Teléfono: {contact[2]},\n"
                        f"Email: {contact[3]}\n"
                        f"*************\n")
        self.scrolledtext.insert(tkinter.END, contact_info)
        
    finally:
      conn.close()