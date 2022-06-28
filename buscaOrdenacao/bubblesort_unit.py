import pytest

import selecao_direta


class Teste:
    @pytest.fixture()
    def unitario(self):
        return selecao_direta.Ordenador()

    def teste1(self, unitario):
        assert unitario.selecaoDireta([5, 2, 1, 3, 4])
