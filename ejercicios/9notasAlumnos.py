'''
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
'''

lista_nombres, lista_notas = [], []

for i in range(4):
  nombre = str(input("Introduce el nombre del alumno: "))
  nota = float(input("Introduce la nota: "))
  
  lista_nombres.append(nombre), lista_notas.append(nota)

sobresaliente = 0

for j in range(4):
  print(lista_nombres[j])
  print(lista_notas[j])
  
  if lista_notas[j] >= 8:
    print("Muy bueno")
    sobresaliente += 1
  elif 4 <= lista_notas[j] < 8:    # lista_notas <= 4 and lista_notas <= 7
    print("Bueno")
  elif lista_notas[j] < 4:
    print("Insuficiente")
print(f"Cantidad de sobresalientes: {sobresaliente}")