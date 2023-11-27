'''
38.- Implementar un programa que permita introducir 2 números en controles de tipo Entry para, posteriormente, sumar ambos valores ingresados y mostrar la suma en una Label al presionar un botón.
'''

import tkinter as tkinter

class Aplicacion:
  
  def __init__(self):
    self.ventana = tkinter.Tk()
    self.ventana.title("Aplicación")  # título de la ventana
    
    self.valor1 = tkinter.Label(self.ventana, text="Primer valor: ")
    self.valor2 = tkinter.Label(self.ventana, text="Segundo valor: ")
    
    self.valor1.grid(column=0, row=0)
    self.valor2.grid(column=0, row=1)
    
    self.dato1 = tkinter.IntVar()
    self.entrada1 = tkinter.Entry(self.ventana)
    self.entrada1.grid(column=1,row=0)
    
    self.dato2 = tkinter.IntVar()
    self.entrada2 = tkinter.Entry(self.ventana)
    self.entrada2.grid(column=1, row=1)
    
    self.boton_suma = tkinter.Button(self.ventana, text="Sumar", command=self.suma)
    self.boton_suma.grid(column=0, row=2)
    
    self.ventana.mainloop()
  
  def suma(self):
    self.total = (int(self.entrada1.get()) +
                  int(self.entrada2.get()))
    self.label_suma = tkinter.Label(self.ventana, text=self.total)
    self.label_suma.grid(column=1, row=2)
    
aplicacionChunga = Aplicacion()