
def calcular_valor_total(valor_unitario: float, quantidade: int) -> float:

    desconto = 1

    if quantidade >= 10 and quantidade <= 99:
        desconto = 0.95
    elif quantidade >= 100 and quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85

    valor_com_desconto = valor_unitario * desconto * quantidade
    valor_sem_desconto = valor_unitario * quantidade

    return valor_sem_desconto, valor_com_desconto

if __name__ == '__main__':
    valor_unitario = float(input('Valor unitário do produto: '))
    quantidade = int(input('Quantidade: '))

    valor_sem_desconto, valor_com_desconto = calcular_valor_total(valor_unitario, quantidade)

    print(f'Valor total sem desconto: {valor_sem_desconto:.2f} R$')
    print(f'Valor total com desconto: {valor_com_desconto:.2f} R$')