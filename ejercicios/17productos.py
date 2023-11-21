'''
17.- Almacenar los nombres de 5 productos y sus precios.
Utilizar una lista y cada elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
        1) Cargar por teclado.
        2) Listar los productos y precios.
        3) Imprimir los productos con precios comprendidos entre 10 y 15.
'''

productos = [("Chirimoyas", 2.99),("Kakis", 14.99), ("Patatas", 10.99), ("Kiwis", 1.9), ("Pimientos", 3.99)]

def imprimir():
  for item in range(len(productos)):
    print(productos[item])
    
imprimir()

def precios():
  for nombre, precio in productos:
      if precio >= 10 and precio <= 15:
        print(f"{nombre} - {precio}")
      
precios()