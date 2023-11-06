'''
Crear un programa en el que pida una oración por teclado,
la cual puede tener letras tanto en mayúsculas como minúsculas.
Contar la cantidad de vocales. Crear un segundo string con toda la
oración en minúsculas para que sea
más fácil disponer la condición que verifica que es una vocal.
'''

frase = str(input("Introduce tu frase para "
                  "contar las vocales: "
                  "\n")).lower()
def suma_vocales(frase):
  vocales = 0
  for vowel in frase:
    if vowel in "aeiouáéíóú":
      vocales += 1
  return vocales

print("Tu frase en minúscula: ", frase)
print(f"Número de vocales: {suma_vocales(frase)}")