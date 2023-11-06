'''
14.- Plantear una función que reciba un string en
mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'.
'''

string = str(input("Introduce la frase: ")).lower()

def contar_a(frase):
  contador = 0
  for letra in frase:
    if letra == "a":
      contador += 1
  print(contador)  #o return contador

contar_a(string)
# if return contador:
#   contador = contar_a(string)
#   print(contador