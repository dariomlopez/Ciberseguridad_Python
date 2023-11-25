'''
34.- Crear 2 objetos de la clase Button con las etiquetas: "chico" y "chica", al presionarse mostrar en la barra de títulos de la ventana la etiqueta del botón presionado.
'''

import tkinter as tkinter

class Botones:
  def __init__(self):
    # Creación de la ventana
    self.ventana = tkinter.Tk()
    # Medidas de la ventana
    self.ventana.geometry("350x250")
    
    # Botón1 que llama a la función Chico
    self.boton1 = tkinter.Button(self.ventana, text="Chico", command=self.Chico)
    #  Colocamos el botón1
    self.boton1.grid(column=0, row=0)
    
    # Botón2 que llama a la función Chica
    self.boton2 = tkinter.Button(self.ventana, text="Chica", command=self.Chica)
    # Colocamos el botón2
    self.boton2.grid(column=1, row=0)
    
    self.ventana.mainloop()
    
    
  # Cambiamos el título de la ventana y el Label según pulsemos un botón u otro
  def Chico(self):
    self.label1 = tkinter.Label(self.ventana, text="Has pulsado chico")
    self.ventana.title("Has pulsado chico")
    self.label1.grid(column=0, row=1)
  
  def Chica(self):
    self.label2 = tkinter.Label(self.ventana, text="Has pulsado chica")
    self.ventana.title("Has pulsado chica")
    self.label2.grid(column=0, row=1)
    
botones = Botones()