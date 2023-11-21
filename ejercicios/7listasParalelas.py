'''
Crear dos listas paralelas.
En la primera ingresar los nombres de empleados y
en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)
'''

empleados = []
lista_sueldos = []
posicion = 0

num_empleados = int(input("Ingresa el número de empleados: "))

for num in range(num_empleados):
  nombres = str(input("Ingresa el nombre del empleado: "))
  sueldo = float(input("Ingresa el sueldo del empleado: "))
  empleados.append(nombres)
  lista_sueldos.append(sueldo)
  
while posicion < len(lista_sueldos):
  if lista_sueldos[posicion] > 1000:
    empleados.pop(posicion)
    lista_sueldos.pop(posicion)
  else:
    posicion += 1
    
print("Empleados que cobran menos de 1000€ al mes")
for i in range(len(lista_sueldos)):
    print(f"Empleado: {empleados[i]} - Sueldo: {lista_sueldos[i]}")