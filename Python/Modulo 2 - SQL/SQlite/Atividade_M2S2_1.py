'''
Crie um programa em Python que gere tabelas para uma aplicação de gerenciamento de tarefas. As tabelas devem compreender as seguintes funcionalidades:
As tarefas devem ser divididas em “categorias”;
Uma tarefa deve ter nome, data, categoria e status de conclusão (se foi realizada ou não); 
As restrições/relacionamentos devem fazer sentido.

'''


import sqlite3
# criando uma conexão 

conexao = sqlite3.connect('gerenciamento_tarefas.sqlite3')
cursor = conexao.cursor()
    
# criando tabela de categorias
    
sql = '''
CREATE TABLE categorias (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT(50) NOT NULL,
    CONSTRAINT categorias_UN UNIQUE (nome)
)
'''
cursor.execute(sql)

# criando tabela de tarefas

sql1 = '''
CREATE TABLE tarefas (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT(100) NOT NULL,
	data TEXT(10),
	categorias_id INTEGER NOT NULL,
	status INTEGER NOT NULL,
	CONSTRAINT tarefas_FK FOREIGN KEY (categorias_id) REFERENCES categorias(id) ON DELETE SET NULL
)
'''
cursor.execute(sql1)

# commit e fechar a conexão
conexao.commit()
conexao.close()

# Inserir dados de exemplo

conexao = sqlite3.connect('gerenciamento_tarefas.sqlite3')
cursor = conexao.cursor()

# Inserir categorias
cursor.execute("INSERT INTO categorias (nome) VALUES ('Trabalho')")
cursor.execute("INSERT INTO categorias (nome) VALUES ('Estudo')")
cursor.execute("INSERT INTO categorias (nome) VALUES ('Lazer')")

# Inserir tarefas
cursor.execute("INSERT INTO tarefas (nome, data, categoria_id, status) VALUES ('Reunião', '2023-12-12', 1, realizado)")
cursor.execute("INSERT INTO tarefas (nome, data, categoria_id, status) VALUES ('Estudar Python', '2023-12-15', 2, não realizado)")
cursor.execute("INSERT INTO tarefas (nome, data, categoria_id, status) VALUES ('Passear no parque', '2023-12-18', 3, não realizado)")

# Commit e fechar a conexão
conexao.commit()
conexao.close()