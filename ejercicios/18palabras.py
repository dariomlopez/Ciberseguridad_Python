'''
18.- Definir una función que cargue una lista con palabras y la retorne.
- otra función tiene que mostrar todas las
palabras de la lista que tienen más de 5 caracteres.
'''

lista_palabras = []

def palabras():
  num_palabras = int(input("Cuantas palabras quiere: "))
  for iter in range(num_palabras):
    palabra = str(input("Introduce la palabra: "))
    lista_palabras.append(palabra)
  print(lista_palabras)
  
def mas_cinco():
  for palabra in lista_palabras:
    if len(palabra) > 5:
      print(palabra)
  
  
palabras()
mas_cinco()