pecas = []


def gerar_codigo():
    tamanho_lista = len(pecas)
    if tamanho_lista > 0:
        ultima_peca = pecas[tamanho_lista - 1]
        ultimo_codigo = ultima_peca['codigo']
        return ultimo_codigo + 1

    return 1


def cadastrar_peca(nome, fabricante, valor):
    codigo = gerar_codigo()
    print(f'\nCódigo da peça: {codigo:03d}')
    peca = {
        'codigo': codigo,
        'nome': nome,
        'fabricante': fabricante,
        'valor': valor
    }

    pecas.append(peca)
    print('Peça Adicionada!\n')


def imprimir_peca(peca):
    print(f'Código: {peca["codigo"]:03d}')
    print(f'Fabricante: {peca["fabricante"]}')
    print(f'Valor: {peca["valor"]:.2f} R$')


def consultar_pecas(opcao_consulta, codigo=None, fabricante=None):
    if opcao_consulta == 1:
        for peca in pecas:
            imprimir_peca(peca)
            print('-' * 15)
    elif opcao_consulta == 2:
        for peca in pecas:
            if peca['codigo'] == codigo:
                imprimir_peca(peca)
                print('-' * 15)
                break
    elif opcao_consulta == 3:
        for peca in pecas:
            if peca['fabricante'] == fabricante:
                imprimir_peca(peca)
                print('-' * 15)


def remover_peca(codigo):
    peca_remover = None
    for peca in pecas:
        if peca['codigo'] == codigo:
            peca_remover = peca
            break

    if peca_remover:
        pecas.remove(peca_remover)
        print('Peça removida com sucesso')
    else:
        print('Peça não encontrada')


if __name__ == '__main__':
    opcao = 0
    while opcao != 4:
        print('Escolha a opção desejada')
        print('1 - Cadastrar Peças')
        print('2 - Consultar Peças')
        print('3 - Remover Peças')
        print('4 - Sair')
        opcao = int(input('Opção desejada: '))

        if opcao == 1:
            nome = input('Por favor entre com o nome da peça: ')
            fabricante = input('Por favor entre com o fabricante da peça: ')
            valor = float(input('Por favor entre com o valor da peça (R$): '))
            cadastrar_peca(nome, fabricante, valor)
        elif opcao == 2:
            print('Você selecionou a opção para consultar peças')
            print('Escolha a opção desejada:')
            print('1 - Consultar todas as peças')
            print('2 - Consultar peças por código')
            print('3 - Consultar peças por fabricante')
            print('4 - Retornar')
            opcao_consulta = int(input('Opção: '))
            if opcao_consulta in [1, 2, 3]:
                if opcao_consulta == 2:
                    codigo = int(input('Digite o código da peça: '))
                    consultar_pecas(opcao_consulta, codigo)
                elif opcao_consulta == 3:
                    fabricante = input('Digite o fabricante da peça: ')
                    consultar_pecas(opcao_consulta, fabricante)
                else:
                    consultar_pecas(opcao_consulta)
            elif opcao_consulta == 4:
                print()
            else:
                print('Opção inválida. Tente novamente')
        elif opcao == 3:
            codigo = int(input('Código da peça a ser removida: '))
            remover_peca(codigo)
        elif opcao > 4 or opcao < 1:
            print('Opção inválida')

    print('Obrigado por usar nossos aplicativos')
