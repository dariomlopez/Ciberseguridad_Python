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

orden_alfab = sorted(zip(lista_paises, lista_habitantes))

print("Orden alfabético:\n")
for pais, habitantes in orden_alfab:
  print(f"{pais} - {habitantes}")

orden_habitantes = sorted(zip(lista_paises, lista_habitantes),
                          key=lambda x: x[1], reverse=True)

print("\nOrden por cantidad de habitantes\n")
for pais, habitantes in orden_habitantes:
  print(f"{pais} - {habitantes}")