'''
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
 realizar un programa que lea los sueldos que cobra cada empleado e informe
 cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el
 programa deberá informar el importe que gasta la empresa en sueldos al personal.
'''


empleados_cien , empleados_300, sueldo, \
  gasto_sueldo\
  = 0, 0, 0, 0

empleados_totales = int(input("Introduce el "
                        "número de trabajadores "
                              "de tu empresa: "))

for iterador in range(empleados_totales):
  while True:
    try:
      sueldo = int(input("Introduce el sueldo de los "
                 "empleados: "))
      gasto_sueldo += sueldo
      if sueldo >= 100 and sueldo <= 300:
        empleados_cien += 1

      elif sueldo > 300:
        empleados_300 += 1
      break
    except ValueError:
      print("El valor del sueldo debe ser un "
            "número. Intentalo de nuevo")
    
print("Empleados que cobran entre 100$ y 300$: "
      f"{empleados_cien}\n"
      f"Empleados que cobran más de 300$: "
      f"{empleados_300}\n"
      f"Gasto total de la empresa en sueldo: "
      f"{gasto_sueldo}")