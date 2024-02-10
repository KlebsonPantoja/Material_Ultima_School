'''
Uma pessoa do seu time de desenvolvimento está escrevendo várias funções que calculam diferentes formas de gerar juros. Veja abaixo o exemplo de uma das funções:


Ela pediu para você escrever um decorator chamado decorator_imprimir, que será usado para a função chamada imprima os parâmetros: capital, taxa e tempo, além do resultado da função.

Ao executar a função juros_simples, teríamos o seguinte resultado:


Com isso, será criada uma função decoradora (decorator) chamada decorator_imprimir que, ao ser usada com qualquer função parecida com a juros_simples (isto é, uma função que receba 3 parâmetros – capital, taxa, tempo), seja retornado um valor numérico correspondente ao juros.

'''

# CRIANDO A FUNÇÃO DECORATOR_IMPRIMIR

def decorador_imprimir(func):
    def imprimir (capital,taxa,tempo):
        print(f'CAPITAL:{capital} TAXA:{taxa} TEMPO:{tempo}')
        resultado = func(capital,taxa,tempo)
        print(f'RESULTADO:{resultado}')
    return(imprimir)

# UTILIZANDO A FUNÇÃO DECORATOR_IMPRIMIR COM A FUNÇÃO JUROS_SIMPLES

@decorador_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa/100) * tempo

juros_simples(1000, 5, 6)