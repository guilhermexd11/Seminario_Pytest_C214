import Calculadora.calculadora as calc
import pytest

class TesteSoma():

    def test_soma(self):
        assert calc.Calculadora.soma(1, 2) == 3

    def test_soma_negativos(self):
        assert calc.Calculadora.soma(-1, -2) == -3

    def test_soma_zeros(self):
        assert calc.Calculadora.soma(0, 0) == 0

    def test_soma_decimal(self):
        assert calc.Calculadora.soma(1.5, 2.5) == 4.0

    def test_soma_mistos(self):
        assert calc.Calculadora.soma(1, -2) == -1