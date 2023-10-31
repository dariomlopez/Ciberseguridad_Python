espacios = 0

frase = str(input("Introduce una frase: "))

for letra in frase:
  if letra in " ":
    espacios += 1

print(espacios)