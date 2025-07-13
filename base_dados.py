import sqlite3

conexao = sqlite3.connect("base_dados.db")
cursor = conexao.cursor()


def criar_tabela():
    cursor.execute(
        "CREATE TABLE clientes ("
        "id integer PRIMARY KEY AUTOINCREMENT,"
        " cpf integer,"
        " nome text,"
        " senha text,"
        " nascimento date,"
        " endereco text)"
    )

def inserir_dados_clientes(cpf, nome, senha, nascimento, endereco):
    cursor.execute(
        "INSERT INTO clientes (cpf, nome, senha, nascimento, endereco)"
        " VALUES (?,?,?,?,?)",
        (cpf, nome, senha, nascimento, endereco)
    )
    conexao.commit()

