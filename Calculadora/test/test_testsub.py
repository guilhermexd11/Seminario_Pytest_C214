import Calculadora.calculadora as calc
import pytest

class TestSubtração():
    
    def test_subtracao(self):
        assert calc.Calculadora.subtracao(9, 3) == 6

    def test_subtracao_negativos(self):
        assert calc.Calculadora.subtracao(-5, -2) == -3

    def test_subtracao_zeros(self):
        assert calc.Calculadora.subtracao(0, 0) == 0

    def test_subtracao_decimal(self):
        assert calc.Calculadora.subtracao(5.5, 2.5) == 3.0

    def test_subtracao_mistos(self):
        assert calc.Calculadora.subtracao(1, -2) == 3