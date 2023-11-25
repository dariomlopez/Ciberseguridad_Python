'''
36.- Confeccionar una aplicación que permita introducir un entero por teclado y al presionar un botón muestre dicho valor elevado al cuadrado en una Label.
'''


from tkinter import *

root = Tk()

root.title("titulo")

mensaje = Label(root, text="información")

mensaje.pack()

root.mainloop()