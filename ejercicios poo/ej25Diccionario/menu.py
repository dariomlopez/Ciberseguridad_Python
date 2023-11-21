import diccionario
diccionario = diccionario.Diccionario()

def menu():
  opcion = 0
  while opcion != 5:
    print(
      """
      Introduce la opción:
      1 - Carga de documento y nombre en el diccionario.
      2 - Listado completo del diccionario.
      3 - Consulta ingresando el documento de la persona.
      4 - Finalizar programa
      """)
    opcion = int(input("Opción: "))
    if opcion == 1:
      diccionario.agregar()
    elif opcion == 2:
      diccionario.mostrar_diccionario()
    elif opcion == 3:
      diccionario.buscar_nombre()
    elif opcion == 4:
      print("Cerrando aplicación...Adios")
      break
    else:
      print("Opción invalida. Intentalo de nuevo: ")
      menu()
      
menu()