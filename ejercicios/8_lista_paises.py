'''
Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo.
- Ordenar alfabéticamente
    e imprimir los resultados.
- Por último ordenar por cantidad de habitantes (de mayor a menor) e
    imprimir nuevamente.
'''

lista_paises, lista_habitantes = [], []

for i in range(5):
  pais = str(input("Introduce el nombre del pais: "))
  habitantes = int(input("Introduce el número de habitantes: "))
  
  lista_paises.append(pais)
  lista_habitantes.append(habitantes)

lista_paises.sort(), lista_habitantes.sort()
print(f"{lista_paises} {lista_habitantes}")
