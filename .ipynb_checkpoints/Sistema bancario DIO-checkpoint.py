# --------------------------------------------- Importações ---------------------------------------------

from dataclasses import dataclass

# --------------------------------------------- Classes ---------------------------------------------

@dataclass
class Cliente:
    nome: str
    senha: str
    nascimento: str
    cpf: str
    endereco: str

# --------------------------------------------- Funções ---------------------------------------------
    
def deposito():
    
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        
        print("Operação falhou! O valor informado é inválido.")


    
def saque():
    
    valor = float(input("Informe o valor do saque: "))

    if valor > saldo:
        print("A operação falhou! Saldo insuficiente.")       
    elif valor > limite:
        print("Operação falhou! Limite de saque atingido.")
    elif numero_saques >= limite_saque:
        print("Operação falhou! Você atingiu o limite de saques da sua conta!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")


    
def extrato():  
    print("\n================ EXTRATO ================")
    print(f"\nO plano selecionado foi: {cestas_disponiveis[opcao_cesta["Cesta Selecionada"]]}")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {(saldo - tarifa):.2f}")
    print("===========================================")

def cesta_servicos():

    cestas_disponiveis = ["Prata", "Ouro", "Diamante"]
    opcao_cesta = {}
                       
    plano = input("""

    Selecione o tipo de plano desejado:
    
    [1] Prata: 3 saques, R$ 10.00.
    [2] Ouro: 5 saques, R$ 15.00.
    [3] Diamante: 10 saques, R$ 20.00.
    
    => """)

    match plano:

        case "1":
            limite_saque = 3
            tarifa = 10
            cesta_selecionada = 0
            if numero_saques >= limite_saque:
                print("Plano excedido, escolha outro plano")
            else:
                opcao_cesta.setdefault("Limite de saques", limite_saque)
                opcao_cesta.setdefault("Tarifa", tarifa)
                opcao_cesta.setdefault("Cesta selecionada", cesta_selecionada)
            exit()
        case "2":
            limite_saque = 5
            tarifa = 15
            cesta_selecionada = 1
            if numero_saques >= limite_saque:
                print("Plano excedido, escolha outro plano")
            else:
                opcao_cesta.setdefault("Limite de saques", limite_saque)
                opcao_cesta.setdefault("Tarifa", tarifa)
                opcao_cesta.setdefault("Cesta selecionada", cesta_selecionada)
            exit()
        case "3":
            limite_saque = 10
            tarifa = 20
            cesta_selecionada = 2
            if numero_saques >= limite_saque:
                print("Plano excedido, escolha outro plano")
            else:
                opcao_cesta.setdefault("Limite de saques", limite_saque)
                opcao_cesta.setdefault("Tarifa", tarifa)
                opcao_cesta.setdefault("Cesta selecionada", cesta_selecionada)
            exit()
        case _:
            print("Por favor, selecionar um dos números")
            exit()

def cadastrar_cliente():
    return Cliente(
        nome = input("Insira seu nome: ").strip(),
        senha = input("Informe a senha desejada: ").strip(),
        nascimento = input("Insira sua data de nascimento: ").strip(),
        cpf = input("Informe o seu CPF: ").strip(),
        endereco = input("Informe seu endereço: ").strip()
    )
    

def login_cliente():
    
    cpf = input("Bem vindo cliente, insira seu cpf ").strip()
    senha = input("Insira sua senha!").strip()
    
    for i in base_clientes:
        if i.cpf == cpf and i.senha == senha:
            return True
        else:
            return False

# --------------------------------------------- Variáveis globais ---------------------------------------------

plano = "1"
limite_saque = 3
tarifa = 10

saldo = 0
limite = 500

extrato = ""
base_clientes = []

# --------------------------------------------- Código Principal ---------------------------------------------

while True:

    menu = input("""
             
    Escolha a opção desejada:
    
    [1] Entrar
    [2] Cadastrar-se
    [3] Sair
    
    => """)
    
    if menu == "1":
        if login_cliente() == True:
            
            opcao = input("""

            Bem vindo ! Escolha o que deseja fazer.
            
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [4] Alterar plano
            [0] Sair
            
            => """)
            
            if opcao == "1":
                deposito()
            elif opcao == "2":
                saque()
            elif opcao == "3":
                extrato()
            elif opcao == "4":
                cesta_servicos()
            elif opcao == "0":
                exit()
            else:
                print("por favor, selecione uma opção válida")
        else:
            print("Login falhou, tente novamente!")

    if menu == "2":
        
        cliente = cadastrar_cliente()
        base_clientes.append(cliente)
        
    if menu == "3":
        exit()