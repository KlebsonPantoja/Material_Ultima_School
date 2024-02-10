def imprimir(cardapio):
    print(cardapio)

def calcular_total(pedidos):
    total = 0
    for pedido in pedidos:
        total += pedido['preco']
    return total

def validar_codigo(codigo):
    codigos_validos = {'100', '101', '102', '103', '104', '105', '200', '201'}
    return codigo in codigos_validos

def processar_pedido(codigo):
    cardapio = {
        '100': {'descricao': 'Cachorro Quente', 'preco': 9.00},
        '101': {'descricao': 'Cachorro Quente Duplo', 'preco': 11.00},
        '102': {'descricao': 'X-Egg', 'preco': 12.00},
        '103': {'descricao': 'X-Salada', 'preco': 12.00},
        '104': {'descricao': 'X-Bacon', 'preco': 14.00},
        '105': {'descricao': 'X-Tudo', 'preco': 17.00},
        '200': {'descricao': 'Refrigerante Lata', 'preco': 5.00},
        '201': {'descricao': 'Chá Gelado', 'preco': 4.00}
    }
    return cardapio.get(codigo)

def main():
    cardapio = """
    *******************Cardápio*******************
    ----------------------------------------------
    | Código | Descrição | Valor |
    | 100 | Cachorro Quente | 9,00 |
    | 101 | Cachorro Quente Duplo | 11,00 |
    | 102 | X-Egg | 12,00 |
    | 103 | X-Salada | 12,00 |
    | 104 | X-Bacon | 14,00 |
    | 105 | X-Tudo | 17,00 |
    | 200 | Refrigerante Lata | 5,00 |
    | 201 | Chá Gelado | 4,00 |
    ----------------------------------------------
    """
    imprimir(cardapio)

    pedidos = []
    while True:
        codigo = input('Entre com o código desejado: ')
        if not validar_codigo(codigo):
            print('Opção inválida')
            continue

        pedido = processar_pedido(codigo)
        print(f'Você pediu um {pedido["descricao"]} no valor de {pedido["preco"]:.2f}')
        pedidos.append(pedido)

        pedir_mais = input('Deseja pedir mais alguma coisa? (1 - Sim / 2 - Não): ')
        if pedir_mais == '2':
            break

    total = calcular_total(pedidos)
    print(f'O total a ser pago é: {total:.2f} R$')