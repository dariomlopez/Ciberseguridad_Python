import socket
# import sys


def bannerGrabber(ip):
  results = {}
  with open("C:/Users/junky/Desktop/Ciberseguridad y hacking/Python/hack101/tkinter_grabbing/ports.txt", "r") as ports:
    for port in ports:
      port = int(port.strip())
      try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
          sock.settimeout(10)
          sock.connect((ip, port))
          results[port] = sock.recv(1024).decode("utf-8", errors="ignore")
      
      except socket.error as err:
        results[port] = f"Error: {str(err)}"
      
  return results