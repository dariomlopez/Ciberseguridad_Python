'''
19.- Almacenar en una lista 5 empleados, cada elemento de la lista
es una sub lista con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en una tupla).
El programa debe tener las siguientes funciones:
       1)Carga de los nombres de empleados y sus últimos tres sueldos.
       2)Imprimir el monto total cobrado por cada empleado.
       3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser similar a:
empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]
'''

lista_empleados = []

def cargar_nombres():
  datos_empleado = []
  nombre = str(input("Introduzca el nombre de empleado: "))
  datos_empleado.append(nombre)
  sueldo1 = float(input(f"Introduzca sueldo 1 de {nombre}"))
  sueldo2 = float(input(f"Introduzca sueldo 2 de {nombre}"))
  sueldo3 = float(input(f"Introduzca sueldo 3 de {nombre}"))
  tupla_sueldos = (sueldo1, sueldo2, sueldo3)
  datos_empleado.append(tupla_sueldos)
  lista_empleados.append(datos_empleado)

def cantidad_total():


def ingresos_mayores():