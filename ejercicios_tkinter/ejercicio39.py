'''
39.- Introducir el nombre de usuario y clave en controles de tipo Entry.
Si se ingresa las cadena (usuario: juan, clave="abc123"),
mostrar en el título de la ventana el mensaje "Correcto" en caso contrario mostrar el mensaje "Incorrecto". Para mostrar ** cuando se ingresa la clave debemos pasar en el parámetro 'show' el carácter a mostrar: show="*"
'''

import tkinter as tkinter

class Login:
  
  def __init__(self):
    # ventana principal
    self.ventana = tkinter.Tk()
    self.ventana.title("Login churrigueresco")
    self.ventana.geometry("400x400")
    
    self.label_usuario = tkinter.Label(self.ventana, text="Introduce el usuario: ")
    self.label_password = tkinter.Label(self.ventana, text="Introduce la contraseña: ")
    
    self.label_usuario.grid_configure(column=0, row=0)
    self.label_password.grid_configure(column=0, row=1)
  
    self.usuario = tkinter.StringVar()
    self.password = tkinter.StringVar()
    
    self.entry_user = tkinter.Entry(self.ventana, width=35, textvariable=self.usuario)
    self.entry_password = tkinter.Entry(self.ventana, width=35,
                                        textvariable=self.password, show="*")
    
    self.entry_user.grid_configure(column=1, row=0)
    self.entry_password.grid_configure(column=1, row=1)
    
    self.login_button = tkinter.Button(self.ventana, text="Login", command=self.validation)
    self.login_button.grid_configure(column=0, row=3)
    
    self.ventana.mainloop()
  
  def validation(self):
    usuario = self.entry_user.get()
    password = self.entry_password.get()
    
    if usuario == "juan" and password == "abc123":
      self.message = tkinter.Label(self.ventana, text="Login Correcto")
      self.message.grid_configure(column=1, row=3)
    else:
      self.message = tkinter.Label(self.ventana, text="Login Incorrecto")
      self.message.grid_configure(column=1, row=3)
    


login = Login()