'''
10.- Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es ""
'''

espacios = 0

frase = str(input("Introduce una frase: "))
# recorremos la frase
for letra in frase:
  # Si la letra es un espacio entra en el if y
  # cuenta un espacio
  if letra in " ":
    espacios += 1

print(espacios)