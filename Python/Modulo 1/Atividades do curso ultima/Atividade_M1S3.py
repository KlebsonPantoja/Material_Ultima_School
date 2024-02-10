# Exercicio 1
'''
1. Crie uma função que, ao receber um número inteiro, retorna se um número é par ou ímpar.

Dicas:

– Utilize o comando int(input()) para obter o número inteiro de entrada.

– Passe o número para uma função por parâmetro.

– Calcule e retorne o resultado.

– Mostre na tela se o número é ‘Par’ ou ‘Impar’, usando o comando print().

– Extra: utilize **kwargs (Opcional)

ENTRADA	SAÍDA ESPERADA
2	Par
9	Impar
14	Par

'''
def imp_par ():
    if (numero % 2) == 0:
        return "Seu numero é par!"
    else:
        return"Seu numero é impar!"

numero = int(input("Digite o numero desejado:"))
resultado = imp_par (numero)
print = resultado 

#Exercício 2
'''
2. Crie uma função que recebe um número inteiro por parâmetro e então imprime na tela do número recebido até o zero.

Dicas:

– Utilize o comando int(input()) para obter o número inteiro de entrada.

– Passe o número para uma função por parâmetro.

– Mostre na tela do número recebido até o zero, usando o comando print().

– Extra: crie uma versão recursiva deste programa (Opcional)

ENTRADA	SAÍDA ESPERADA
2	210
5	543210

'''
def ate_zero(numero):
    while numero >= 0:
        print(numero)
        numero -= 1
numero = int(input("Digite um numero: "))
ate_zero(numero)  

#Exercício 3
'''
Crie um programa com uma função que necessite de três parâmetros e então que retorne a sua soma.

Dicas:

– Utilize o comando int(input()) para obter os três números inteiros de entrada.

– Passe os três números para uma função por parâmetro.

– Calcule a soma e retorne o resultado.

– Mostre na tela a soma calculada, usando o comando print().

– Extra: utilize *args (Opcional)

'''
def soma_3_numeros(num1, num2, num3):
    return num1 + num2 + num3

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
print(soma_3_numeros(num1, num2, num3))

#Exercício 4
'''
4. Crie um programa que seja capaz de obter e somar TODOS os números passados pelo usuário como entrada, permitindo somar qualquer quantidade de dados de entrada.

Dicas:

– Utilize uma estrutura de repetição para repetir a leitura de todos os números passados como entrada, até que encontre o valor ‘-1’.

– Ou seja, o número -1 será o critério de parada para a leitura dos dados de entrada.

– Utilize o comando int(input()) para obter todos os números inteiros de entrada.

– Calcule a soma de todos os números.

– Mostre na tela a soma calculada, usando o comando print().

– Extra: utilize Funções e *args (Opcional).

ENTRADA	SAÍDA ESPERADA
27-1	9
472191-1	33
285134316-1	51

'''
soma = 0
numero = int(input("Digite um número: "))
while (numero != -1):
    soma += numero
    numero = int(input("Digite um número: "))
print(soma)

#Exercício 5
'''
Faça um programa com uma função que necessite de um parâmetro. A função deve retornar “Positivo”, se seu o número for maior que zero, “Negativo” se o número for menor que zero, e “Zero” se o número for igual a zero.

Dicas:

– Utilize o comando int(input()) para obter o número inteiro de entrada.

– Implemente uma função que seja capaz de descobrir se um número é positivo, negativo ou zero, e retorne o resultado.

– Mostre na tela o resultado, usando o comando print().

ENTRADA	SAÍDA ESPERADA
2	Positivo
-7	Negativo
0	Zero

'''
def pos_neg_zero(numero):
    numero = int(input("Digite um número: "))
    if numero < 0:
        return "Negativo"
    elif numero > 0:
        return "Positivo"
    elif numero == 0:
        return "Zero"

print(pos_neg_zero(numero))

def positivo_negativo_zero(numero):
  if numero == 0:
    return "Zero"
  elif numero > 0:
    return "Positivo"
  else:
    return "Negativo"

numero = int(input("Digite um número: "))
print(positivo_negativo_zero(numero))

#Exercício 6
'''
6. Escreva uma função que, dado o valor da conta de um restaurante e um percentual de taxa de serviço, calcule e exiba a gorjeta do garçom, considerando o percentual do valor da conta.

Dicas:

– Utilize o comando float(input()) para obter o valor da conta.

– Utilize o comando int(input()) para obter o valor da taxa de serviço.

– Implemente uma função que calcule a gorjeta do garçon, baseado no percentual do valor da conta definido.

– Mostre na tela o resultado com duas casas decimais, usando o comando print(f”{resultado:.2f}”).

– Lembrando que o cálculo de porcentagem é: valor*porcentagem/100.

ENTRADA	SAÍDA ESPERADA
10015	15.00
139.4512	16.73
1529.3227	412.92

'''
def gorjeta(valor, porcentagem):
    return valor*porcentagem/100

valor_conta = float(input('Digite o valor da conta:'))  
porcentagem = int(input('Digite o valor do percentual:'))
resultado = gorjeta(valor_conta, porcentagem)
print(f"{resultado:.2f}")

#Exercício 7
'''

7. Crie uma função que permita contar o número de vezes que aparece uma determinada letra em uma frase. A letra desejada e a frase a ser verificada serão passadas por parâmetro para a função, que retornará a quantidade da letra na frase.

Dicas:

– Utilize o comando input() para obter a letra desejada.

– Utilize o comando input() para obter a frase desejada.

– Implemente uma função que conte a quantidade de vezes que a letra aparece na frase e retorne este valor.

– Mostre na tela o resultado obtido, usando o comando print().

ENTRADA	SAÍDA ESPERADA
aaaaaaa	6
pparalelepipedo	3
nbanana	2

'''
def contagem(letra_buscada, frase):
    contagem = 0
    for letra_atual in frase:
        if letra_atual == letra_buscada:
            contagem += 1
    return contagem
letra = input("Digite a letra: ")
frase = input("Digitea frase: ")
saida = contagem(letra, frase)
print(saida)

#Exercício 8
'''
8. Crie uma função que receba duas palavras e retorne “True” caso a primeira palavra seja um prefixo da segunda, e “False” caso contrário.

Exemplo: ’programa’ é prefixo de “programador”, pois todas as letras de ‘programa’ correspondem às primeiras letras de “programador”.

Dicas:

– Utilize o comando input() para obter a palavra1.

– Utilize o comando input() para obter a palavra2.

– Implemente uma função que identifique se a palavra1 é prefixo da palavra 2, e retorne o resultado obtido.

– Mostre na tela o resultado, usando o comando print().

– Extra: utilize slicing para indexar as strings. (Opcional).

ENTRADA	SAÍDA ESPERADA	EXPLICAÇÃO
programaprogramador True	As 8 letras de programa são exatamente as 8 primeiras letras de programador, então é prefixo!
abcdabcdefghijk	True	As 4 primeiras letras de “abcd” são exatamente as 4 primeiras letras de “abcdefghijk”, então é prefixo!
canabanana	False	Embora 3 das 4 letras de “cana” sejam iguais as 4 primeiras letras de “banana”, era preciso que todas fossem iguais para ser prefixo. Ou seja, não é prefixo!
testatestemunha	False	Embora 4 das 5 letras de “testa” sejam iguais as 5 primeiras letras de “testemunha”, era preciso que todas fossem iguais para ser prefixo. Ou seja, não é prefixo!


'''
def ver_prefixo(palavra1, palavra2):
    tamanho = len(palavra1)
    for indice in range(tamanho):
        if palavra1[indice] != palavra2[indice]:
            return False
    return True  

palavra1 = input("Digite a palavra 1: ")
palavra2 = input("Digite a palavra 2: ") 
resultado = ver_prefixo(palavra1, palavra2)