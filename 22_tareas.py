'''
Crear un menú en el que realicemos las tareas más típicas con las listas:
- crear,
- añadir elemento/s,
- borrar elemento/s,
- borrar lista,
- ordenar elementos de mayor a menor y
- ordenar elementos de menor a mayor
'''

print("""
Introduce la opción:
1 - Crear lista
2 - añadir elemento
3 - añadir elemento por posición
4 - borrar elemento
5 - borrar lista
6 - ordenar elementos de mayor a menor
7 - ordenar elementos de menor a mayor
""")
def crear_lista():
  # crear lista
  lista = []
  return lista
 
def add_element(lista):
  # añadir elemento
  elemento = input("Introduce un elemento")
  lista.append(elemento)

# borrar elemento
def borrar_elemento(lista):
  elemento = input("Introduce un elemento a eliminar")
  if elemento in lista:
    lista.remove(elemento)
    print(lista)

# ordenar
def ordenarMayor(lista):
  lista.sort(reverse = True)
  return lista
  
# ordenar de menor a mayor
def ordenarMayor(lista):
  lista.sort()
  return lista

# borrar lista
def borrar_lista(lista):
  lista.clear()
  return lista