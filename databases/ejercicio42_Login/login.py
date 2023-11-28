import tkinter as tkinter
import sqlite3
from tkinter.messagebox import showinfo, showerror


class Login:
  
  def __init__(self):
    self.ventana = tkinter.Tk()
    self.ventana.title("Login")
    self.ventana.geometry("300x250")
    
    self.label_user = tkinter.Label(self.ventana, text="Usuario")
    self.label_user.pack()
    self.user_entry = tkinter.Entry(self.ventana)
    self.user_entry.pack()
    
    self.label_passw = tkinter.Label(self.ventana, text="Password")
    self.label_passw.pack()
    self.passw_entry = tkinter.Entry(self.ventana)
    self.passw_entry.pack()
    
    self.boton_login = tkinter.Button(self.ventana, text="Login", command=self.login)
    self.boton_login.pack()
    
    self.ventana.mainloop()
    
  def login(self):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    
    usuario = self.user_entry.get()
    passw = self.passw_entry.get()
    
    try:
      cursor.execute("""
      select * from usuarios where usuario = ? and password = ?
      """, (usuario, passw))
      
      if cursor.fetchall():
        showinfo(title="Login correcto", message="Entrando...")
      else:
        showerror(title="Login incorrecto", message="Usuario o contraseña incorrecto")
    
    except sqlite3.OperationalError as err:
      print("la tabla ya existe", err)
    
    cursor.close()

login = Login()