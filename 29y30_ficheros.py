'''
29.- Crear un archivo de texto llamado 'datos.txt', almacenar tres líneas de texto y, posteriormente, leer el archivo en cuesión
Sentinel — hoy a las 13:01
30.- Abrir el archivo de texto 'datos.txt' y luego agregar 2 líneas. Imprimir luego el archivo completo.
'''

archivo = open("datos.txt", "w")

archivo.write("If you really really want \n"
              "what you really really want \n"
              "if you wanna be my lover\n")
with open("datos.txt", "r") as archivo:
  mensaje = archivo.read()

archivo.close()
print(mensaje)

with open("datos.txt", "a") as archivo:
  archivo.writelines("oaoaoaaoaoaoaoa \n"
                "oaoaoaoaoaoaoao \n"
                "aaaaaaaaaaaaaaaa")

with open("datos.txt", "r") as archivo:
  mensaje = archivo.read()

archivo.close()
print(mensaje)