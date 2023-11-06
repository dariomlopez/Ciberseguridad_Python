'''
Solicitar por teclado el ingreso de una clave por
teclado y almacenarla en una cadena de caracteres.
Controlar que el string ingresado tenga entre
10 y 20 caracteres para que sea válido,
 en caso contrario mostrar un mensaje de error.
'''

clave = ""

while len(clave) < 10 or len(clave) > 20:
  clave = str(input("Ingresa la clave:\n"))
  if len(clave) >= 10 and len(clave) <= 20:
    print("Clave correcta. Guardando clave...")
  else:
    print(
      "La clave debe tener una longitud entre 10 "
      "y 20 caracteres.\n")
    clave = str(input("Intentalo de nuevo:\n"))