
# EXEMPLO 1
def maiusculo(texto):
    return texto .upper()

print(maiusculo('ultima'))
mensagemMaiusculo = maiusculo
print(mensagemMaiusculo('school'))

# EXEMPLO 2

def somador(x):
    def soma(y):
        return x+y
    return soma

resultado = somador (15)

print (resultado(10))

# EXEMPLO 3

def cumprimento(funcao):
    def saudacao():
        print('Bom Dia !')
        funcao()
        print('Boa Noite !')
    return saudacao

@cumprimento
def boa_tarde():
    print('Boa Tarde !')

boa_tarde()

# PRIMEIRO DECORADOR DE FUNÇÃO

def primeiro_decorador(func):
    def primeira_func():
        print('Execução antes da Função')

        func()

        print('Execução depois da Função')
    return primeira_func
def funcao_utilizadora():
    print('Presciso utilizar o decorador')
final = primeiro_decorador(funcao_utilizadora)

final()


