'''
35.- Mostrar los botones del 1 al 5. Cuando se presiona mostrar en una Label todos los botones presionados hasta ese momento.
'''

import tkinter as tkinter

class App:
  def __init__(self):
    self.boton_pulsado = ""
    
    self.ventana = tkinter.Tk()
    self.ventana.title = "Númericos"
    self.ventana.geometry("200x200")
    
    self.boton1 = tkinter.Button(self.ventana, text=1, command=self.Press1)
    self.boton1.grid(column=0, row=0)
    
    self.boton2 = tkinter.Button(self.ventana, text=2, command=self.Press2)
    self.boton2.grid(column=1, row=0)
    
    self.boton3 = tkinter.Button(self.ventana, text=3, command=self.Press3)
    self.boton3.grid(column=2, row=0)
    
    self.boton4 = tkinter.Button(self.ventana, text=4, command=self.Press4)
    self.boton4.grid(column=0, row=1)
    
    self.boton5 = tkinter.Button(self.ventana, text=5, command=self.Press5)
    self.boton5.grid(column=1, row=1)
    
    self.label = tkinter.Label(self.ventana, text =
      str(self.boton_pulsado))
    self.label.grid(column=0, row=2)
  
    self.ventana.mainloop()
  def Press1(self):
    self.boton_pulsado += "1"
    self.label.configure(text=self.boton_pulsado)
  def Press2(self):
    self.boton_pulsado += "2"
    self.label.configure(text=self.boton_pulsado)
  def Press3(self):
    self.boton_pulsado += "3"
    self.label.configure(text=self.boton_pulsado)
  def Press4(self):
    self.boton_pulsado += "4"
    self.label.configure(text=self.boton_pulsado)
  def Press5(self):
    self.boton_pulsado += "5"
    self.label.configure(text=self.boton_pulsado)
  
  

app = App()