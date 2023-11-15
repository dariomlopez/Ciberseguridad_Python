'''
32.- Generar tantos archivos como letras del abecedario, todos con formato txt.
'''

for char in 'abcdefghijklmnopqrstuvwxyz':
  with open(f"{char}.txt", "w") as file:
    file.write(str(char))