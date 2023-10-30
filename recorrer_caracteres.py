mensaje = str(input("Introduce el mensaje: "))

for posicion in range(len(mensaje)):
  print(f"Letra: "
        f"{mensaje[posicion]}. Posición: {posicion}")