import pytest

import Bhaskara


class TestBhaskara:

    @pytest.fixture()  # Guarda o objeto antes declarado
    def b(self):
        return Bhaskara.Bhaskara()

    def testa_raiz(self, b):
        assert b.calcula_raiz(1, 0, 0) == (1, 0)

    def testa_duas_raizes(self, b):
        assert b.calcula_raiz(1, -5, 6) == (2, 3, 2)

    def testa_zero_raizes(self, b):
        assert b.calcula_raiz(10, 10, 10) == 0


