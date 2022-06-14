def ordenada(lista):
    fim = len(lista)
    for i in range(fim - 1):
        pos_minimo = i  # o menor e i
        for j in range(i + 1, fim):  # percorre a lista ate o fim
            if lista[j] <= lista[pos_minimo]:
                return False
            else:
                return True
    if fim <= 2:
        return True


lista = []

ordenada(lista)
