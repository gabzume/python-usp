import pytest


def fibonnaci(n):
    if n < 2:  ## Base da recursao (caso mais simples)
        return n
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)  ## Chamada recursiva


@pytest.mark.parametrize("entrada, esperado", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5)])
def testa(entrada, esperado):
    assert fibonnaci(entrada) == esperado
