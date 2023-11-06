espacios = 0

frase = str(input("Introduce una frase: "))
# recorremos la frase
for letra in frase:
  # Si la letra es un espacio entra en el if y
  # cuenta un espacio
  if letra in " ":
    espacios += 1

print(espacios)