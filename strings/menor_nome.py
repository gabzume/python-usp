nomes = ['ana', 'giovanna', 'melissa', 'gustavo']

def menorNome(lista1):
    for i in lista1:
        menor = min(lista1)
        alt = menor.capitalize().strip()
    return alt


print(menorNome(nomes))
