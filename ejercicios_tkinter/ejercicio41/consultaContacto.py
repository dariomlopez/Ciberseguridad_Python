# -*- coding: utf-8 -*-
import sqlite3
import tkinter as tkinter
from tkinter import messagebox
from tkinter import scrolledtext as st

class ConsultarContacto(tkinter.Frame):
  def __init__(self, parentTab):
    super().__init__(parentTab)
    
    self.label_id = tkinter.Label(self, text="Introduce el id del contacto a buscar")
    self.label_nombre = tkinter.Label(
      self, text="Introduce el nombre que quieres buscar: ")
    self.label_telf = tkinter.Label(self, text="Teléfono que quieres buscar: ")
    self.label_email = tkinter.Label \
      (self, text="Email que quieres buscar: ")
    
    self.id = tkinter.IntVar()
    self.nombre = tkinter.StringVar()
    self.telefono = tkinter.IntVar()
    self.email = tkinter.StringVar()
    
    self.entry_id = tkinter.Entry(self, textvariable=self.id)
    self.entry_nombre = tkinter.Entry(
      self, width=25, textvariable=self.nombre)
    self.entry_telf = tkinter.Entry \
      (self, width=25, textvariable=self.telefono)
    self.entry_email = tkinter.Entry \
      (self, width=25, textvariable=self.email)
    
    self.label_id.pack()
    self.entry_id.pack()
    self.label_nombre.pack()
    self.entry_nombre.pack()
    self.label_telf.pack()
    self.entry_telf.pack()
    self.label_email.pack()
    self.entry_email.pack()
    
    
    self.botonBuscar = tkinter.Button(self, text="Buscar", command=self.buscarContacto)
    self.botonBuscar.pack()
    
    self.scrolledtext = st.ScrolledText(self)
    self.scrolledtext.pack()
    
  def buscarContacto(self):
    id = self.entry_id.get()
    nombre = self.entry_nombre.get()
    telf = self.entry_telf.get()
    email = self.entry_email.get()
    
    conn = sqlite3.connect("C:/Users/junky/Desktop/Ciberseguridad y hacking/Python/ejercicios_tkinter/ejercicio41/agendaDB.db")
    cursor = conn.cursor()

    if id or nombre or telf or email:
      query= f"""
        select *
        from agenda
        where id = ?
        or nombre = ?
        or telefono = ?
        or email = ?
      """
      params = (id, nombre, telf, email)
      cursor.execute(query, params)
      resultado = cursor.fetchall()
      self.scrolledtext.delete("1.0", tkinter.END)
      for idx, contact in enumerate(resultado):
        contact_info = (f"ID: {contact[0]},\n"
                        f"Nombre: {contact[1]},\n"
                        f"Teléfono: {contact[2]},\n"
                        f"Email: {contact[3]}\n")
        self.scrolledtext.insert(tkinter.END, contact_info)
    else:
      messagebox.showerror("Buscar contacto", "No se han ingresado criterios de busqueda")
   
    conn.close()
  