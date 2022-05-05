m1 = [[1, 2]]
m2 = [[1, 2]]

def soma_matrizes(matriz1, matriz2):
    tam = len(matriz1)
    if any(len(lst) != tam for lst in [matriz1, matriz2]):
        return False
    else:
        for i in matriz1:
            total = []
            zipa1 = zip(matriz1[0], matriz2[0])
            zipa2 = zip(matriz1[1], matriz2[1])
            som = [x + y for (x, y) in zipa1]
            som2 = [x + y for (x, y) in zipa2]
            total.append(som)
            total.append(som2)
            print(total)


soma_matrizes(m1, m2)

