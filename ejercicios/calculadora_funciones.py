operacion = ""
def suma():
  print(num1 + num2)
def resta():
  print(num1 - num2)
def division():
  print(num1 / num2)
def multiplicacion():
  print(num1 * num2)

while operacion != "t":
  num1 = float(input("Introduce el primer "
                     "número: "))
  num2 = float(
    input(
      "Introduce el segundo número "
      "número: "))
  operacion = str(
    input(
      "Introduce la operación "
      "aritmetica deseada o 't' para terminar: ")).lower()
  
  if operacion == "+":
    suma()
  elif operacion == "-":
    resta()
  elif operacion == "/":
    division()
  elif operacion == "*":
    multiplicacion()
  elif operacion == "t":
    print("Finalizando")
    exit()
  else:
    print("Operación no admitida")