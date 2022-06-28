class Buscador:
    def busca(lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        else:
            return False

    def buscaBinaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista)-1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo)//2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return -1


lista = [-100, 0, 10, 300, 500, 5000]
b = Buscador()
print(f'Posição: {b.buscaBinaria(lista, 5000)}')
