import pytest
from frete import calcular_preco_volume, calcular_multiplicador_peso, calcular_multiplicador_rota

def test_calcular_preco_volume():
    assert calcular_preco_volume(999) == 10.0
    assert calcular_preco_volume(1000) == 20.0
    assert calcular_preco_volume(10000) == 30.0
    assert calcular_preco_volume(30000) == 20.0

def test_calcular_multiplicador_peso():
    assert calcular_multiplicador_peso(0.05) == 1.0
    assert calcular_multiplicador_peso(0.5) == 1.5
    assert calcular_multiplicador_peso(5) == 2.0
    assert calcular_multiplicador_peso(20) == 3.0

def test_calcular_multiplicador_rota():
    assert calcular_multiplicador_rota('rs') == 1.0
    assert calcular_multiplicador_rota('sb') == 1.2
    assert calcular_multiplicador_rota('br') == 1.5
    