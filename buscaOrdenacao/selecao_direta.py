class Ordenador:
    def selecaoDireta(self, lista):
        fim = len(lista)
        for i in range(fim - 1):
            pos_minimo = i  # o menor e i
            for j in range(i + 1, fim):  # percorre a lista ate o fim
                if lista[j] < lista[pos_minimo]:
                    pos_minimo = j  # se o elemento de j e menor que o minimo, assume um novo valor, o de j
                    lista[i], lista[pos_minimo] = lista[pos_minimo], lista[i]
            return lista

    def Bolha(self, lista):
        fim = len(lista)
        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    def BolCurta(self, lista):
        fim = len(lista)
        for i in range(fim - 1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocou = True
            if not trocou:
                return



