import sqlite3

conexao = sqlite3.connect("base_dados.sqlite")
cursor = conexao.cursor()

# Modelos de Tabela


def criar_tabela_clientes():
    cursor.execute(
        "CREATE TABLE clientes ("
        "id integer PRIMARY KEY AUTOINCREMENT,"
        "cpf integer,"
        "nome text,"
        "senha text,"
        "nascimento date,"
        "endereco text)"
    )

def criar_tabela_contas():
    cursor.execute(
        "CREATE TABLE contas("
        "conta INTEGER PRIMARY KEY AUTOINCREMENT,"
        "agencia INTEGER,"
        "usuario_id INTEGER,"
        "saldo INTEGER,"
        "limite_saque INTEGER,"
        "numero_saques INTEGER,"
        "tarifa INTEGER,"
        "cesta TEXT,"
        "FOREIGN KEY (usuario_id) REFERENCES clientes(id))")

def criar_tabela_lancamentos():
    cursor.execute(
        "CREATE TABLE lancamentos ("
        "id integer PRIMARY KEY AUTOINCREMENT,"
        "conta integer,"
        "data date,"
        "lancamento text,"
        "valor integer,"
        "FOREIGN KEY (conta) REFERENCES contas(conta))"
    )

# Inserção de dados

def inserir_dados_contas(
        agencia: int,
        usuario_id: int,
        saldo: float,
        limite_saque: int,
        numero_saques: int,
        tarifa: int,
        cesta: str
) -> None:

    cursor.execute(
        "INSERT INTO contas (agencia, usuario_id, saldo, limite_saque, numero_saques, tarifa, cesta) "
        "VALUES (?,?,?,?,?,?,?)",
        (agencia, usuario_id, saldo, limite_saque, numero_saques, tarifa, cesta)
    )
    conexao.commit()

def inserir_dados_extrato(conta, data, lancamento, valor):
    cursor.execute(
        "INSERT INTO lancamentos(conta, data, lancamento, valor) "
        "VALUES (?, ?, ?, ?)",
        (conta, data, lancamento, valor)
    )
    conexao.commit()

# Atualização de dados

def atualizar_saldo(saldo, conta):
    cursor.execute(
        "UPDATE contas SET saldo = ? WHERE conta = ?",
        (saldo, conta)
    )
    conexao.commit()

# Mostrar dados

def mostrar_extrato(conta: int) -> None:
    cursor.execute(
        "SELECT data, lancamento, valor FROM lancamentos WHERE conta = ?",
        (conta,)
    )

    for data, lancamento, valor in cursor.fetchall():
        print(f"{data} | {lancamento} | {valor}")

def mostrar_contas(cpf: int) -> list:
    cursor.execute(
        "SELECT id FROM clientes WHERE cpf = ?",
        (cpf,)
    )
    id_cliente = cursor.fetchone()[0]

    cursor.execute(
        "SELECT * FROM contas where usuario_id = ?",
        (id_cliente,)
    )

    contas = cursor.fetchall()

    return contas

def id_usuario(cpf:int) -> int:
    cursor.execute(
        "SELECT id FROM clientes WHERE cpf = ?",
        (cpf,)
    )
    return cursor.fetchone()[0]

def id_conta(cpf) -> int:
    cursor.execute(
        "SELECT MAX(conta) "
        "FROM contas "
        "LEFT JOIN clientes ON contas.usuario_id = clientes.id "
        "WHERE cpf = ?",
        (cpf,)
    )
    resultado = cursor.fetchone()[0]

    if resultado is None:
        conta_criada = 1
    else:
        conta_criada = resultado + 1

    return conta_criada

# Funções de cadastro e login

def cadastrar_cliente(cpf, nome, senha, nascimento, endereco):
    cursor.execute(
        "INSERT INTO clientes (cpf, nome, senha, nascimento, endereco)"
        " VALUES (?,?,?,?,?)",
        (cpf, nome, senha, nascimento, endereco)
    )
    conexao.commit()

def login(cpf, senha):

    cursor.execute(
        "SELECT senha "
            "FROM clientes "
            "WHERE cpf = ?",
  (cpf,)
    )

    senha_db = cursor.fetchone()

    if senha_db is None:
        print("Usuário não encontrado.")
        return None

    if senha == senha_db[0]:
        print("Login bem sucedido!")
        cursor.execute(
            "SELECT * "
            "FROM clientes "
            "WHERE cpf = (?)",
            (cpf,)
        )

        return cursor.fetchone()


    else:
        print("Acesso negado.")
        return None