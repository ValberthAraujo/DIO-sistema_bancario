import sqlite3

conexao = sqlite3.connect("base_dados.sqlite")
cursor = conexao.cursor()

class Consultas:

    @staticmethod
    def criar_tabela_clientes():
        cursor.execute(
            "CREATE TABLE clientes ("
            "id integer PRIMARY KEY AUTOINCREMENT,"
            " cpf integer,"
            " nome text,"
            " senha text,"
            " nascimento date,"
            " endereco text)"
        )

    @staticmethod
    def criar_tabela_extrato():
        cursor.execute(
            "CREATE TABLE lancamentos ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "usuario_id INTEGER,"
            "data DATE,"
            "lancamento TEXT,"
            "valor INTEGER,"
            "FOREIGN KEY (usuario_id) REFERENCES usuarios(id))"
        )

    @staticmethod
    def inserir_dados_clientes(cpf, nome, senha, nascimento, endereco):
        cursor.execute(
            "INSERT INTO clientes (cpf, nome, senha, nascimento, endereco)"
            " VALUES (?,?,?,?,?)",
            (cpf, nome, senha, nascimento, endereco)
        )
        conexao.commit()