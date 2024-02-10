import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('Atividade_M2S4.sqlite3')
cursor = conexao.cursor()

# Função para criar um TODO
def create_todo(description, due_date=None):
    cursor.execute("INSERT INTO todos (description, due_date) VALUES (?, ?)", (description, due_date))
    conexao.commit()

# Função para atualizar um TODO
def update_todo(todo_id, description=None, due_date=None, is_completed=None):
    update_query = "UPDATE todos SET "
    if description:
        update_query += f"description = '{description}', "
    if due_date:
        update_query += f"due_date = '{due_date}', "
    if is_completed is not None:
        update_query += f"is_completed = {is_completed}, "
    update_query = update_query.rstrip(', ') + f" WHERE todo_id = {todo_id}"

    cursor.execute(update_query)
    conexao.commit()

# Função para excluir um TODO
def delete_todo(todo_id):
    cursor.execute(f"DELETE FROM todos WHERE todo_id = {todo_id}")
    conexao.commit()

# Função para criar uma categoria
def create_category(name):
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
    conexao.commit()

# Função para listar todos os afazeres de um dia específico
def list_todos_by_date(date):
    cursor.execute(f"SELECT * FROM todos WHERE due_date = '{date}'")
    todos = cursor.fetchall()
    return todos

# Função para listar todas as categorias
def list_categories():
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    return categories

# Função para marcar uma tarefa como concluída
def mark_todo_as_completed(todo_id):
    cursor.execute(f"UPDATE todos SET is_completed = 1 WHERE todo_id = {todo_id}")
    conexao.commit()

# Exemplo de uso
create_todo("Completar a atividade", "2023-12-31")
list_all_todos = list_todos_by_date("2023-12-31")
print("Todos para 2023-12-31:", list_all_todos)

# Lembre-se de fechar a conexão quando terminar
conexao.close()