import tkinter as tk

class Aplicacion:

#creación e inicialización de ventana/etiqueta/botones
  def __init__(self):
#Ventana principal (la hemos llamado Ventana1)
    self.valor = 1
    self.ventana1 = tk.Tk()#llamada para creación de ventana
    self.ventana1.title("Controles de BUTTON y LABEL")#título de la ventana

#Label (etiqueta o texto) que hemos llamado Label1
    self.label1 = tk.Label(self.ventana1, text=self.valor)#creación de objeto que
# variará su valor
    self.label1.grid(column=0, row=0)#como tenemos muchas formas de pintar en el monitor, utilizamos un grid (rejilla)
    self.label1.configure(foreground="red")#cambiamos el color de fondo de ese valor, es decir, el color de la fuente que nos muestra el valor

#Button (botón) que hemos llamada boton1 y boton2
    self.boton1 = tk.Button(self.ventana1, text="Incrementar valor ++", command=self.incrementar)
    #nombre_boton = tk.claseBotón(dónde_lo_muestro, text="que texto pongo en el botón", command=lo_que_ejecuto)
    self.boton1.grid(column=0, row=1)

    self.boton2 = tk.Button(self.ventana1, text="Decrementar valor --", command=self.decrementar)
    self.boton2.grid(column=0, row=2)
    
    #lanzamiento de ventana al sistema o monitor
    self.ventana1.mainloop()

  def incrementar(self):
    self.valor = self.valor + 1
    self.label1.config(text=self.valor)
    
  def decrementar(self):
    self.valor = self.valor - 1
    self.label1.config(text=self.valor)

#MAIN
aplicacionchunga = Aplicacion()