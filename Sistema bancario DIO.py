# --------------------------------------------- Importações ---------------------------------------------

from dataclasses import dataclass


# --------------------------------------------- Classes ---------------------------------------------

@dataclass
class Cliente:
    nome: str
    senha: str
    nascimento: str
    endereco: str
    extrato: str
    cpf: int
    cesta: int
    limite_saque_qtd: int
    limite_saque_valor: int
    tarifa: int
    saldo: int
    numero_saques: int

# --------------------------------------------- Variáveis globais ---------------------------------------------

base_clientes = []

# --------------------------------------------- Funções ---------------------------------------------

def validar_input(input__desejado: str, tamanho_variavel: int):
    while True:

        variavel_validada = 0

        try:
            variavel_validada = int(input(input__desejado).strip())

            if tamanho_variavel == 0:
                try:
                    variavel_validada = input__desejado
                except ValueError:
                    print('Digite um valor valido')
            else:
                if variavel_validada < 0 or len(str(variavel_validada)) != tamanho_variavel:
                    raise ValueError

        except ValueError:
            print("Insira corretamente os dados requisitados ")
            continue
        break
    return variavel_validada
    
def deposito(saldo_cliente, extrato_cliente):
    
    valor = int(validar_input("Informe o valor do depósito: ", 0))

    if valor > 0:
        
        saldo_cliente += valor
        extrato_cliente += f"Depósito: R$ {valor:.2f}\n"

    else:
        
        print("Operação falhou! O valor informado é inválido.")

    return saldo_cliente, extrato_cliente

    
def saque(saldo_cliente, extrato_cliente, numero_saques_cliente):
    
    valor = float(input("Informe o valor do saque: "))

    if valor > saldo_cliente:
        print("A operação falhou! Saldo insuficiente.")       
    elif valor > base_clientes[id_cliente].limite_saque_valor:
        print("Operação falhou! Limite de saque atingido.")
    elif numero_saques_cliente >= base_clientes[id_cliente].limite_saque_qtd:
        print("Operação falhou! Você atingiu o limite de saques da sua conta!")
    elif valor > 0:
        saldo_cliente -= valor
        extrato_cliente += f"Saque: R$ {valor:.2f}\n"
        numero_saques_cliente += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo_cliente, extrato_cliente, numero_saques_cliente


    
def mostrar_extrato(extrato_cliente, saldo_cliente):
    
    print("\n================ EXTRATO ================")
    print(f"\nO plano selecionado foi: {base_clientes[id_cliente].cesta}")
    print("Não foram realizadas movimentações." if not extrato_cliente else extrato_cliente)
    print(f"\nSaldo: R$ {(saldo_cliente - base_clientes[id_cliente].tarifa):.2f}")
    print("===========================================")


# noinspection PyUnreachableCode
def cesta_servicos():

    opcao_cesta = {}

    while True:
        plano = input("""

        Selecione o tipo de plano desejado:
    
        [1] Prata: 3 saques, 2000 limite de saque , R$ 10.00.
        [2] Ouro: 5 saques, 5000 limite de saque , R$ 15.00.
        [3] Diamante: 10 saques, 10000 limite de saque , R$ 20.00.
    
        => """)

        # noinspection PyUnreachableCode
        match plano:
            case "1":
                opcao_cesta["Cesta selecionada"] = "Prata"
                opcao_cesta["Limite de saques quantidade"] = 3
                opcao_cesta["Limite de saques valor"] = 2000
                opcao_cesta["Tarifa"] = 10
                return opcao_cesta
            case "2":
                opcao_cesta["Cesta selecionada"] = "Ouro"
                opcao_cesta["Limite de saques quantidade"] = 5
                opcao_cesta["Limite de saques valor"] = 5000
                opcao_cesta["Tarifa"] = 15
                return opcao_cesta
            case "3":
                opcao_cesta["Cesta selecionada"] = "Diamante"
                opcao_cesta["Limite de saques quantidade"] = 10
                opcao_cesta["Limite de saques valor"] = 10000
                opcao_cesta["Tarifa"] = 20
                return opcao_cesta
            case _:
                print("Por favor, selecione uma opção válida")


# noinspection PyTypeChecker
def cadastrar_cliente():
    
    opcao_cesta = cesta_servicos()

    cesta_selecionada = opcao_cesta["Cesta selecionada"]
    limite_saque_qtd = opcao_cesta["Limite de saques quantidade"]
    limite_saque_valor = opcao_cesta["Limite de saques valor"]
    tarifa_selecionada = opcao_cesta["Tarifa"]

    cpf_usuario = validar_input("Insira o seu CPF (apenas números, 11 digitos) ", 11)
    data_nascimento = validar_input("Digite o data de nascimento (DDMMYYYY) ", 8)

    return Cliente(
        nome = input("Insira seu nome: ").strip(),
        senha = input("Informe a senha desejada: ").strip(),
        nascimento = data_nascimento ,
        cpf = cpf_usuario,
        endereco = input("Informe seu endereço: ").strip(),
        cesta = cesta_selecionada,
        limite_saque_qtd = limite_saque_qtd,
        limite_saque_valor = limite_saque_valor,
        tarifa = tarifa_selecionada,
        saldo = 0,
        numero_saques = 0,
        extrato = ""
    )
    

def login_cliente():
    cpf = int(input("Bem vindo cliente, insira seu cpf (apenas números): ").strip())
    senha = input("Insira sua senha: ").strip()

    for i in base_clientes:
        if i.cpf == cpf and i.senha == senha:
            return True, base_clientes.index(i)

    return False, None

# --------------------------------------------- Programa Principal ---------------------------------------------

while True:

    menu = input("""
             
    Escolha a opção desejada:
    
    [1] Entrar
    [2] Cadastrar-se
    [0] Sair
    
    => """)
    
    if menu == "1":
        
        resultado_login, id_cliente = login_cliente()
        
        while resultado_login:
            
            opcao = input(f"""

            Bem vindo {base_clientes[id_cliente].nome}! Escolha o que deseja fazer.
            
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [4] Alterar plano
            [0] Sair

            => """)
            
            if opcao == "1":
                base_clientes[id_cliente].saldo, base_clientes[id_cliente].extrato = deposito(base_clientes[id_cliente].saldo, base_clientes[id_cliente].extrato)
            elif opcao == "2":
                base_clientes[id_cliente].saldo, base_clientes[id_cliente].extrato, base_clientes[id_cliente].numero_saques = saque(base_clientes[id_cliente].saldo, base_clientes[id_cliente].extrato, base_clientes[id_cliente].numero_saques)
            elif opcao == "3":
                mostrar_extrato(base_clientes[id_cliente].extrato, base_clientes[id_cliente].saldo)
            elif opcao == "4":
                dados_cesta = cesta_servicos()

                base_clientes[id_cliente].cesta = dados_cesta["Cesta selecionada"]
                base_clientes[id_cliente].limite_saque_qtd = dados_cesta["Limite de saques quantidade"]
                base_clientes[id_cliente].limite_saque_valor = dados_cesta["Limite de saques valor"]
                base_clientes[id_cliente].tarifa = dados_cesta["Tarifa"]

            elif opcao == "0":
                exit()
            else:
                print("por favor, selecione uma opção válida")
        else:
            print("Login falhou, tente novamente!")

    if menu == "2":
        
        cliente = cadastrar_cliente()
        base_clientes.append(cliente)
        
    if menu == "0":
        exit()
