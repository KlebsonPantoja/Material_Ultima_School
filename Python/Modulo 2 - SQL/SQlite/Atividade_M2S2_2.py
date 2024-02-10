'''
Crie um programa em Python que gere tabelas para uma aplicação de eventos. Elas devem compreender as seguintes funcionalidades:
Eventos devem ter título, data e local, além da referência ao organizador;
O organizador deve ter nome, email e cpf;
As restrições/relacionamentos devem fazer sentido.

'''

import sqlite3
from datetime import datetime

# Função para criar o esquema do banco de dados
def criar_tabelas():
    conexao = sqlite3.connect('gerenciador_eventos.db')
    cursor = conexao.cursor()

    # Tabela de Organizadores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS organizador (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE
        )
    ''')

    # Tabela de Eventos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS evento (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            data TEXT NOT NULL,
            local TEXT NOT NULL,
            organizador_id INTEGER,
            FOREIGN KEY (organizador_id) REFERENCES organizador (id)
        )
    ''')

    conexao.commit()
    conexao.close()

# Função para adicionar um novo evento
def adicionar_evento(titulo, data, local, organizador_nome, organizador_email, organizador_cpf):
    conexao = sqlite3.connect('gerenciador_eventos.db')
    cursor = conexao.cursor()

    # Verifica se o organizador já existe ou o cria
    cursor.execute('INSERT OR IGNORE INTO organizador (nome, email, cpf) VALUES (?, ?, ?)',
                   (organizador_nome, organizador_email, organizador_cpf))

    # Obtém o ID do organizador
    cursor.execute('SELECT id FROM organizador WHERE cpf = ?', (organizador_cpf,))
    organizador_id = cursor.fetchone()[0]

    # Insere o novo evento
    cursor.execute('''
        INSERT INTO evento (titulo, data, local, organizador_id)
        VALUES (?, ?, ?, ?)
    ''', (titulo, data, local, organizador_id))

    conexao.commit()
    conexao.close()

# Função para listar todos os eventos
def listar_eventos():
    conexao = sqlite3.connect('gerenciador_eventos.db')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT evento.id, evento.titulo, evento.data, evento.local, organizador.nome AS organizador
        FROM evento
        JOIN organizador ON evento.organizador_id = organizador.id
    ''')

    eventos = cursor.fetchall()

    for evento in eventos:
        print(f"ID: {evento[0]}, Título: {evento[1]}, Data: {evento[2]}, Local: {evento[3]}, Organizador: {evento[4]}")

    conexao.close()

# Criar as tabelas se não existirem
criar_tabelas()

# Adicionar alguns eventos de exemplo
adicionar_evento("Conferência de Tecnologia", str(datetime.now()), "Centro de Convenções", "João Silva", "joao@email.com", "12345678901")
adicionar_evento("Workshop de Python", str(datetime.now()), "Sala de Treinamento", "Maria Oliveira", "maria@email.com", "98765432109")
adicionar_evento("Conferência de Tecnologia", str(datetime.now()), "Centro de Convenções", "Klebson Pantoja", "pantoja@email.com", "12345678911")
# Listar os eventos
listar_eventos()
