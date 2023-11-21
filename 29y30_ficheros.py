'''
29.- Crear un archivo de texto llamado 'datos.txt', almacenar tres líneas de texto y, posteriormente, leer el archivo en cuesión
Sentinel — hoy a las 13:01
30.- Abrir el archivo de texto 'datos.txt' y luego agregar 2 líneas. Imprimir luego el archivo completo.
'''

archivo = open("datos.txt", "w")

archivo.write("Tras comenzar el día de manera bastante agitada, \n"
              "Arthur empezaba a reunir los fragmentos en que había quedado reducida su mente tras las conmociones de la jornada anterior. \n")
with open("datos.txt", "r") as archivo:
  mensaje = archivo.read()

archivo.close()
print(mensaje)

with open("datos.txt", "a") as archivo:
  archivo.write(" Encontró una máquina Nutrimática que le proveyó de una taza de "
                "plástico llena de un líquido que era casi, pero no del todo, enteramente diferente del té.\n")

with open("datos.txt", "r") as archivo:
  mensaje = archivo.read()

archivo.close()
print(mensaje)