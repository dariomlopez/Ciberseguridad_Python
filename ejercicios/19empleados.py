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

def cargar_datos():
  datos_empleado = []
  for iter in range(5):
    nombre = str(input("Introduzca el nombre de empleado: "))
    sueldo1 = float(input(f"Introduzca sueldo 1 de {nombre}"))
    sueldo2 = float(input(f"Introduzca sueldo 2 de {nombre}"))
    sueldo3 = float(input(f"Introduzca sueldo 3 de {nombre}"))
    datos_empleado.append([nombre, (sueldo1, sueldo2, sueldo3)])
    lista_empleados.append(datos_empleado)
  return lista_empleados

def cantidad_total(lista_empleados):
  for datos in lista_empleados:
      total = sum(datos[1])
  print(f"El empleado {datos[0]} cobra por timestre {total}")

def ingresos_mayores(lista_empleados):
  print("Empleados que han cobrado más de 10.000 en el último trimestre")
  total = 0
  for datos in lista_empleados:
      total = sum(datos[1])
      if total > 10000:
        print(datos[0], total)
        
empleados = cargar_datos()
cantidad_total(empleados)
ingresos_mayores(empleados)
