import Calculadora.calculadora as calc
import pytest

class TesteMultiplicacao():
    
    def test_multiplicacao(self):
        assert calc.Calculadora.multiplicacao(6, 2) == 12

    def test_multiplicacao_negativos(self):
        assert calc.Calculadora.multiplicacao(-3, -4) == 12

    def test_multiplicacao_zeros(self):
        assert calc.Calculadora.multiplicacao(0, 5) == 0

    def test_multiplicacao_decimal(self):
        assert calc.Calculadora.multiplicacao(1.5, 2) == 3.0

    def test_multiplicacao_mistos(self):
        assert calc.Calculadora.multiplicacao(-2, 3) == -6