'''
Un posible candidato a un empleo realiza un test de capacitación,
se obtuvo la siguiente información:
cantidad total de preguntas que se le realizaron y la cantidad de
preguntas que contestó correctamente.
Se pide confeccionar un
 programa que ingrese los dos datos por teclado e informe el nivel
 del mismo según el porcentaje de respuestas correctas que ha obtenido,
 y sabiendo que:
 Nivel máximo:    Porcentaje>=90%
Nivel medio:    Porcentaje>=75% y <90%
Nivel regular:    Porcentaje>=50% y <75%
Fuera de nivel:    Porcentaje<50%.
'''

total_preguntas, nivel, preguntas_correctas = \
  0, 0, 0


while True:
    try:
      total_preguntas = int(input("Introduzca "
                                  "el número de preguntas que se"
                                  " le hicieron "
                                  "al "
                                  "candidato: "))
      preguntas_correctas = int(input(
        "Introduzca número de preguntas "
        "correctas: "))
      nivel = (preguntas_correctas /
               total_preguntas) * 100
      
      if nivel >= 90:
        print("El candidato está en el nivel "
              "máximo")
      elif 75 <= nivel < 90:
        print("El candidato está en el nivel "
              "medio")
      elif 50 <= nivel < 75:
        print("El candidato está en el nivel "
              "regular")
      else:
        print("El candidato esta fuera de nivel")
      break
    except ValueError:
      print("Debe introducir un número entero")

