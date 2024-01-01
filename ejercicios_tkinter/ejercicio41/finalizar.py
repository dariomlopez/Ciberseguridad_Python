#finalizar_agenda 

import tkinter as tkinter


class Finalizar(tkinter.Frame):
  def __init__(self, parentTab):
    super().__init__(parentTab)
    self.botonExit = tkinter.Button(self, text="Salir", command=self.end_of_it_all)
    
    self.botonExit.pack()
  
  def end_of_it_all(self):
    self.botonExit.destroy()
    self.botonExit.quit()