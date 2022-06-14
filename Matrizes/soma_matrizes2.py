m1 = [[1, 2, 3], [1, 2, 3]]
m2 = [[1, 2, 3], [1, 2, 3]]


def soma_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return False
    result = []
    for i in range(len(matriz1)):
        result.append([])
        for j in range(len(matriz1[0])):
            result[i].append(matriz1[i][j] + matriz2[i][j])
            # soma e o nosso retorno, result
    return result


print(soma_matrizes(m1, m2))

