'''
Crie uma tabela chamada “cliente”. É necessário que ela tenha as seguintes colunas:

ID
NOME
CPF
DATA_CADASTRO
ENDERECO

'''

import sqlite3
conexao = sqlite3.connect('Atividade_M2S1.sqlite3')
cursor = conexao.cursor()
sql = '''
CREATE TABLE cliente(
	ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	NOME TEXT(100),
	CPF TEXT(11),
	DATA_CADASTRO TEXT,
	ENDEREÇO TEXT
)
'''
cursor.execute(sql)
conexao.commit()
conexao.close()