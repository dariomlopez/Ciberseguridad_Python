'''
Crear un programa con la siguiente información:

Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.
'''

edad_manana, edad_tarde, edad_noche, total, iterador = 0, \
  0, 0, 0, 0
promedio_manana, promedio_tarde, promedio_noche\
  = 0, 0, 0
fin = ""

for iterador in range(5):
    while True:
      try:
        edad_manana = int(input("Introduce la edad de los "
                                "alumnos de la mañana: "))
        total += edad_manana
        break
      except ValueError:
        print("Introduce un número por favor")
    promedio_manana = total / 5
print(f"Promedio de la mañana: "
            f"{round(promedio_manana)} años")
total = 0
  
for iterador in range(6):
    while True:
      try:
        edad_tarde = int(
          input(
            "Introduce la edad de "
            "los alumnos de la "
            "tarde: "))
        total += edad_tarde
        break
      except ValueError:
        print("Introduce un número por favor")
    promedio_tarde = total / 6
print(f"Promedio de la tarde: "
            f"{round(promedio_tarde)} años")
total = 0
  
for iterador in range(11):
    while True:
      try:
        edad_noche = int(
          input(
            "Introduce la edad de "
            "los alumnos de la "
            "noche: "))
        total += edad_noche
        break
      except ValueError:
        print("Introduce un número por favor")
    promedio_noche = total / 11
    print(total)
print(f"Promedio de la noche: "
            f"{round(promedio_noche)} años")
total = 0
  
if promedio_noche > promedio_manana and \
    promedio_noche > promedio_tarde:
    print("El promedio de edad del turno de noche es mayor")
  
elif promedio_tarde> promedio_manana and \
      promedio_tarde > promedio_noche:
    print(
      "El promedio de edad del turno de tarde es "
      "mayor")
    
else:
    print("El promedio de edad del turno de "
          "mañana es mayor")