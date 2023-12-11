import socket
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# rango de direcciones IP
for host in range(1, 255):
  # leer los puertos del archivo ports
  ports = open("ports.txt", "r")
  # leer el archivo con banners vulnerables
  vulnbanners = open("vulnbanners.txt", "r")
  
  # leer los puertos en ports.txt
  for port in ports:
    try:
      socket.connect((str(sys.argv[1])+'.'+str(host), int(port)))
      print(f" Contectando a: {str(sys.argv[1])}.{str(host)}. "
            f"Puerto: {str(port)}")
      # podemos darle tiempo de espera (milisegundos):
      socket.settimeout(2000)
      #Recibimos la respuesta en un Megabyte(1024)
      banner = socket.recv(1024).decode("utf-8")
      # leer los banners vulnerables del archivo vulnbanners
      for vulnbanner in vulnbanners:
        # si el banner está en la lista de vulnerables
        if banner.strip() in vulnbanner.strip():
          print(f"Banner vulnerable: {banner}\n"
                f"Host objetivo: {str(sys.argv[1])}.{str(host)}\n"
                f"Puerto: {str(port)}")
    # en caso de error en el bloque anterior:
    except:
      print(f"Error al intertar conectar a: {str(sys.argv[1])}.{str(host)}. "
            f"Puerto: {str(port)}")
      pass