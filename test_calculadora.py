import pytest
import calculadora

def test_soma():
    assert calculadora.somar(5, 5) == 10

def test_subtracao():
    assert calculadora.subtrair(4, 2) == 2

def test_multiplicacao():
    assert calculadora.multiplicar(5, 10) == 50

def test_divisao():
    assert calculadora.dividir(20, 10) == 2

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        assert calculadora.dividir(5, 0)