import shodan

SHODAN_API_KEY = "Fp59COO5MMYFOAt0uPqC5zKkOnIJl18R"
api = shodan.Shodan(SHODAN_API_KEY)

try:
  query = str(input("Introduce lo que quieres buscar en shodan: "))
  results = api.search(f"{query}")
  
  print(f"Resultados encontrados: {results["total"]}")
  for result in results["matches"]:
    print(f"IP: {result["ip_str"]}")
    print(result["data"])
    print("")
    
except shodan.APIError as err:
  print(f"Error: {err}")