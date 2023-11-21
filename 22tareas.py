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
8 o 0 - cerrar la aplicación
""")
    
def crear_lista():
  # crear lista
  lista = []
  return lista
 
def add_element(lista):
  # añadir elemento
  elemento = input("Introduce un elemento: ")
  lista.append(elemento)
  return lista

# borrar elemento
def borrar_elemento(lista):
  elemento = input("Introduce un elemento a eliminar: ")
  if elemento in lista:
    lista.remove(elemento)
    print(lista)
  return lista
    
# borrar elemento por posición
def borrar_posicion(lista):
  posicion = input("Introduce un elemento a eliminar por posicion: ")
  if posicion >= 0 and posicion < len(lista):
    lista.pop(posicion)
    print(lista)
  else:
    print("Posición fuera de rango")
  return lista

# ordenar
def ordenarMayor(lista):
  lista.sort(reverse = True)
  print(lista)
  return lista

# ordenar de menor a mayor
def ordenarMenor(lista):
  lista.sort()
  print(lista)
  return lista

# borrar lista
def borrar_lista(lista):
  lista.clear()
  print(f"Lista vacia: {lista}")
  return lista

opcion = 0
while opcion != 8 or opcion != 0:
  opcion = int(input("Introduce la opción: "))
  if opcion == 1:
    crear_lista()
  elif opcion == 2:
    add_element()
  elif opcion == 3:
    borrar_elemento()
  elif opcion == 4:
    borrar_posicion()
  elif opcion == 5:
    ordenarMayor()
  elif opcion == 6:
    ordenarMenor()
  elif opcion == 7:
    borrar_lista()
  elif opcion == 8:
    print("Cerrando aplicación...adios")
    break
  else:
    print("La opción elegida no existe")