
'''
import pytest
from gestao_de_pecas import gerar_codigo, cadastrar_peca, consultar_pecas, remover_peca

def test_gerar_codigo():
    assert gerar_codigo() == 1

def test_consultar_pecas():
    cadastrar_peca('Peça Teste 1', 'Fabricante Teste', 10.50)
    cadastrar_peca('Peça Teste 2', 'Fabricante Teste', 20.75)
    cadastrar_peca('Peça Teste 3', 'Outro Fabricante', 30.25)

    assert consultar_pecas(1) is None  # Não testa a saída, apenas se a função não gera erro
    assert consultar_pecas(2, 2) is None  # Não testa a saída, apenas se a função não gera erro
    assert consultar_pecas(3, fabricante='Fabricante Teste') is None  # Não testa a saída, apenas se a função não gera erro

def test_remover_peca():
    cadastrar_peca('Peça Teste', 'Fabricante Teste', 10.50)
    remover_peca(1)

    # Após remover a peça, consultamos todas as peças para verificar se a remoção foi bem-sucedida
    assert consultar_pecas(1) == None

'''
    
# tipo de teste 2

'''
import pytest
from gestao_de_pecas import gerar_codigo, cadastrar_peca, imprimir_peca

def test_gerar_codigo():
    global pecas
    pecas = []
    assert gerar_codigo() == 1
    pecas.append({'codigo': 1})
    assert gerar_codigo() == 1

def test_cadastrar_peca(monkeypatch, capsys):
    global pecas
    pecas = []
    nome = 'Peça 1'
    fabricante = 'Fabricante 1'
    valor = '50'
    entradas = [nome, fabricante, valor]
    monkeypatch.setattr('builtins.input', lambda _: entradas.pop(0))
    cadastrar_peca()
    assert len(pecas) == 0

def test_imprimir_peca(capsys):
    global pecas
    pecas = [{'codigo': 1, 'nome': 'Peça 1', 'fabricante': 'Fabricante 1', 'valor': 50.0}]
    imprimir_peca(pecas[0])
    out, _ = capsys.readouterr()
    assert 'Código: 001\n' in out
    assert 'Fabricante: Fabricante 1\n' in out
    assert 'Valor: 50.00 R$\n' in out

'''