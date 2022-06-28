import selecao_direta
import random
import time


class Contador:
    def aleatoria(self, n):
        lista = [0 for x in range(n)]
        return lista

    def quase_ord(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(self, n):
        lista1 = self.aleatoria(n)
        lista2 = lista1[:]
        o = selecao_direta.Ordenador()

        print("Comparando com listas aleatorias")
        antes = time.time()
        o.BolCurta(lista1)
        depois = time.time()
        print(f'Bolha curta levou {depois - antes} segundos.')

        antes = time.time()
        o.selecaoDireta(lista2)
        depois = time.time()
        print(f'Selecao levou {depois - antes} segundos')

        print("Comparando com listas quase ordenadas")
        lista1 = self.quase_ord(n)
        lista2 = lista1[:]
        antes = time.time()
        o.BolCurta(lista1)
        depois = time.time()
        print(f'Bolha curta levou {depois - antes} segundos.')

        antes = time.time()
        o.selecaoDireta(lista2)
        depois = time.time()
        print(f'Selecao levou {depois - antes} segundos')



c = Contador()

print(c.compara(5000))