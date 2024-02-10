import pytest
from gestao_de_pecas import gerar_codigo, cadastrar_peca, consultar_pecas, remover_peca

def test_gerar_codigo():
    assert gerar_codigo() == 1

def test_consultar_pecas():
    cadastrar_peca('Peça Teste 1', 'Fabricante Teste', 10.50)
    cadastrar_peca('Peça Teste 2', 'Fabricante Teste', 20.75)
    cadastrar_peca('Peça Teste 3', 'Outro Fabricante', 30.25)
    assert consultar_pecas(1) is None  
    assert consultar_pecas(2, 2) is None  
    assert consultar_pecas(3, fabricante='Fabricante Teste') is None  

def test_remover_peca():
    cadastrar_peca('Peça Teste', 'Fabricante Teste', 10.50)
    remover_peca(1)
    assert consultar_pecas(1) == None

