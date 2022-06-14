matriz = [[1, 2, 3, 4], [3, 4, 5, 6], [2, 5, 6, 7]]


def dimensoes(m):
    if len({len(i) for i in m}) > 1:
        print('Matriz errada.')
    linhas = len(m)

    colunas = len(m[0])

    print(f'{linhas}X{colunas}')


dimensoes(matriz)

