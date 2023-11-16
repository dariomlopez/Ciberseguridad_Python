'''
33.- Calcular el número de caracteres de un archivo (creadlo antes en formato TXT)
'''

fichero = open("macondo.txt", "r")
caracteres = 0
for linea in fichero:
  # imprime en consola el contenido del archivo
  print(linea)
  if "\n" in linea:
    print("\n")
  caracteres += len(linea)
  
print(caracteres)

fichero.close()
#
# with open("macondo.txt", "r") as fichero:
#   mensaje = fichero.read()
# fichero.close()
#
# print(mensaje)