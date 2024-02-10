'''
Nesta semana, a última do Módulo 1, vamos criar uma CLI (Command Line Interface) aplicando os conceitos aprendidos nas últimas 4 aulas.

Você foi contratado (a) como programador (a) do Ultima-Bank, o melhor banco da América Latina!

O Ultima-Bank ainda é um banco novo, então alguns processos internos ainda estão sendo realizados de maneira manual, com muita papelada envolvida!

Para agilizar os processos internos, você foi encarregado (a) de desenvolver um sistema de cadastro de novos clientes utilizando Python!
Você entregará nesta tarefa apenas um protótipo para o cadastro de 5 clientes, e caso dê certo, expandiremos para todos os milhões de clientes do Ultima-Bank.

Os dados a serem salvos são:

Nome (String)
CPF (String)
Idade (Inteiro)
Dicas:

Você pode criar uma lista para adicionar todos os clientes;
Você pode usar um dicionário para armazenar cada cliente;
Você vai obter os dados pela entrada padrão (usando a função input()).
Extra (Opcional): Desenvolver utilizando classes.
Saída do seu programa:

Você deve mostrar a seguinte mensagem para cada cliente: print(“Cliente:”, cliente[“Nome”], “CPF:”, cliente[“CPF”], “Idade:”, cliente[“Idade”])
Por exemplo: Cliente: John Snow CPF: 963.125.345-78 Idade: 24
Mostre os cinco clientes, um após o outro.

Além disso, desenvolva um programa que receba dados de clientes e armazene-os em uma lista. A saída do seu programa será os dados formatados dos 5 clientes cadastrados.

'''
class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
# Lista para armazenar os clientes
clientes = []

# Exemplo para 5 clientes
for i in range(5):
    print(f"Digite os dados do Cliente {i + 1}:")
    
    nome = input("Nome: ")
    cpf = input("CPF: ")
    idade = int(input("Idade: "))
    
     # Cliente com os dados fornecidos
    cliente = Cliente(nome, cpf, idade)
    
    # Cliente adicionado a à lista de clientes
    clientes.append(cliente)

# Dados formatados dos 5 clientes
for cliente in clientes:
    print("Cliente:", cliente.nome, "CPF:", cliente.cpf, "Idade:", cliente.idade)
