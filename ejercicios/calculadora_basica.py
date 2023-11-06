operacion = ""

while operacion != "t":
  print(f"### Menu ###"
        f"Elige dos números y '+', '-', '/' o "
        f"'*' para hacer una operación")
  num1 = float(
    input("Introduce el primer número: "))
  num2 = float(
    input(
      "Introduce el segundo "
      "número: "))
  operacion = str(
    input(
      "Introduce la operación "
      "aritmetica deseada o 't' para terminar: "))
  '''sueldo = (
    input("Pulsa 't' para finalizar")).lower()'''
  if operacion == "+":
    print(f"La suma de los números es: "
          f"{num1 + num2}")
  elif operacion == "-":
    print(
      f"La resta de los números es: "
      f"{num1 - num2}")
  elif operacion == "/":
    print(
      f"La división de los números es: "
      f"{num1 / num2}")
  elif operacion == "*":
    print(
      f"La multiplicación de los números es: "
      f"{num1 / num2}")
  else:
    print("Operador no admitido")