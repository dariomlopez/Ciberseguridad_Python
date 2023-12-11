import tkinter as tkinter


class ModificarContacto(tkinter.Frame):
  def __init__(self, parentTab):
    super().__init__(parentTab)
    # tabAgregar = ttk.Label(parentTab, text="Agregar contacto")
    self.label_nombre = tkinter.Label(
      self, text="Introduce el nombre del contacto que quieres "
                 "modificar: ")
    self.label_telf = tkinter.Label(
      self, text="Teléfono que quieres buscar: ")
    self.label_email = tkinter.Label \
      (self, text="Email que quieres buscar: ")
    
    self.nombre = tkinter.StringVar()
    self.telefono = tkinter.IntVar()
    self.email = tkinter.StringVar()
    
    self.entry_nombre = tkinter.Entry(
      self, width=25, textvariable=self.nombre)
    self.entry_telf = tkinter.Entry \
      (self, width=25, textvariable=self.telefono)
    self.entry_email = tkinter.Entry \
      (self, width=25, textvariable=self.email)
    
    self.label_nombre.pack()
    self.entry_nombre.pack()
    self.label_telf.pack()
    self.entry_telf.pack()
    self.label_email.pack()
    self.entry_email.pack()
    
    self.botonBuscar = tkinter.Button(self, text="Buscar")
    self.botonBuscar.pack()