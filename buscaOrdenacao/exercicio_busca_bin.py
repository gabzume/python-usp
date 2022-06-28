def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista)-1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        for i in range(meio, ultimo+1):
            print(i)
            break
        if lista[meio] == elemento:
            return meio
        else:
            if elemento < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return False


lista = []
busca(lista, 0)