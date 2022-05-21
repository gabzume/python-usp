nomes = ["LU   ", " josé ", "PAULO", "Catarina"]

def print_menor_nome(names):
    cleaned_names = [n.strip().lower() for n in names]
    shortest_name = min(cleaned_names, key=len)
    print(f"{shortest_name.capitalize()}")

print_menor_nome(nomes)