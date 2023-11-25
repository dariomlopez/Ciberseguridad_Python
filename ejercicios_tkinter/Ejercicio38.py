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
    self.entrada1 = tkinter.Entry(self.dato1)
    
    self.ventana.mainloop()
    
    
aplicacionChunga = Aplicacion()