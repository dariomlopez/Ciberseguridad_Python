'''
36.- Confeccionar una aplicación que permita introducir un entero por teclado y al presionar un botón muestre dicho valor elevado al cuadrado en una Label.
'''


import tkinter as tkinter

class App:
  def __init__(self):
    self.ventana = tkinter.Tk()
    self.ventana.geometry("200x200")
    
    self.entry = tkinter.Entry(self.ventana)
    self.entry.grid(column=0, row=0)
    #self.valor = self.entry.get()
    
    
    self.boton = tkinter.Button(self.ventana, text="Elevar al cuadrado", command=self.cuadrado)
    self.boton.grid(column=0, row=1)
    
    # self.label = tkinter.Label(self.ventana, text=self.valor)
    # self.label.grid(column=0, row=2)
  
    self.ventana.mainloop()
  def cuadrado(self):
    self.valor = int(self.entry.get())
    self.valor **= 2
    self.label = tkinter.Label(self.ventana, text=self.valor)
    self.label.grid(column=0, row=2)
    
    
app = App()