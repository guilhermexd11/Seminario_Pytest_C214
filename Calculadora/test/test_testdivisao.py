import Calculadora.calculadora as calc
import pytest

class TesteDivisao():

    def test_divisao(self):
        assert calc.Calculadora.divisao(10, 2) == 5

    def test_divisao_negativos(self):
        assert calc.Calculadora.divisao(-8, -2) == 4

    def test_divisao_decimal(self):
        assert calc.Calculadora.divisao(5.5, 2) == 2.75

    def test_divisao_mistos(self):
        assert calc.Calculadora.divisao(8, -2) == -4

    def test_divisaoZero(self):
        assert calc.Calculadora.divisao(10, 0) == True