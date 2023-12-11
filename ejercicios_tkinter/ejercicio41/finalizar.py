#finalizar_agenda 

import tkinter as tkinter


class Finalizar(tkinter.Frame):
  def __init__(self, parentTab):
    super().__init__(parentTab)
    self.botonExit = tkinter.Button(self, text="Salir")
    
    self.botonExit.pack()