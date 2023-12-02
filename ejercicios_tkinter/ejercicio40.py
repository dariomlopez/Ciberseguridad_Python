'''
40.- Implementar 3 controles de tipo Radiobutton con las etiquetas 'Rojo', 'Verde' y 'Azul'. Cuando se presione un botón cambiar el color de fondo del formulario. Si consideramos que la variable ventana1 es un objeto de la clase Tk, si queremos que el fondo sea de color rojo debemos llamar al método configure y en el parámetro bg indicar un string con el color a activar ("red", "green" o "blue"): bg="red"
'''

import tkinter as tkinter

class App:
  def __init__(self):
    self.ventana = tkinter.Tk()
    self.ventana.geometry("200x200")
    
    self.color = tkinter.IntVar()
    self.color.set(1)
    
    self.rojo = tkinter.Radiobutton(self.ventana, text="Rojo", value=1,
                                    variable=self.color,
                                    command=self.cambiar_bg)
    self.rojo.pack()
    
    self.verde = tkinter.Radiobutton(self.ventana, text="Verde", value=2,
                                     variable=self.color,
                                     command=self.cambiar_bg)
    self.verde.pack(padx=10)
    
    self.azul = tkinter.Radiobutton(self.ventana, text="Azul", value=3,
                                    variable=self.color,
                                    command=self.cambiar_bg)
    self.azul.pack()
    
    self.ventana.mainloop()
    
  def cambiar_bg(self):
    if self.color.get() == 1:
      self.ventana.configure(bg="red")
    if self.color.get() == 2:
      self.ventana.configure(bg="green")
    if self.color.get() == 3:
      self.ventana.configure(bg="blue")
    
    
  
app = App()