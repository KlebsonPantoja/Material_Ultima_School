import pytest
from lanche import calcular_total, validar_codigo, processar_pedido

def test_calcular_total():
    pedidos = [
        {'descricao': 'Cachorro Quente', 'preco': 9.00},
        {'descricao': 'X-Egg', 'preco': 12.00}
    ]
    assert calcular_total(pedidos) == 21.00

def test_validar_codigo():
    assert validar_codigo('100') == True
    assert validar_codigo('999') == False

def test_processar_pedido():
    assert processar_pedido('100') == {'descricao': 'Cachorro Quente', 'preco': 9.00}
    assert processar_pedido('999') == None  # Código inválido