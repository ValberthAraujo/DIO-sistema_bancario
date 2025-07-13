from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Cliente:
    cpf: int
    nome: str
    senha: str
    nascimento: int
    endereco: str

    @staticmethod
    def cadastrar_cliente(cpf_usuario):

        data_nascimento = input("Digite a data de nascimento (DDMMYYYY)")

        if len(data_nascimento) != 8:
            print("Digite corretamente a data de nascimento")
            exit()

        data_nascimento = int(data_nascimento)

        for i in base_clientes:
            if i.cpf == cpf_usuario:
                print("CPF já cadastrado, entre em contato conosco! ")
                exit()

        while True:

            logradouro = input("Informe seu logradoro: ").strip()
            bairro = input("Informe seu bairro: ").strip()
            cidade = input("Informe sua cidade: ").strip()
            estado = input("Informe seu estado: ").strip()

            endereco_usuario = f"{logradouro}, {bairro} - {cidade}/{estado}"

            resposta = input(
                "O endereço:\n"
                f"{endereco_usuario}\n"
                "está correto?\n\n"
                "[1] Sim\n"
                "[2] Não\n\n"
                "=> "
            )

            if resposta == "1":
                break
            else:
                continue

        return Cliente(
            cpf=cpf_usuario,
            nome=input("Insira seu nome: ").strip(),
            senha=input("Informe a senha desejada: ").strip(),
            nascimento=data_nascimento,
            endereco=endereco_usuario,
        )

    @staticmethod
    def novo_cliente():

        cpf_usuario = input("Insira o seu CPF "
                            "(apenas números, 11 digitos) ")

        if len(cpf_usuario) != 11:
            print("Digite o cpf corretamente")
            exit()

        pessoa = Cliente.cadastrar_cliente(cpf_usuario)
        conta_usuario = Conta.cadastrar_conta(cpf_usuario)

        return pessoa, conta_usuario

    @staticmethod
    def login_cliente():
        cpf = int(input("Bem vindo cliente, "
                        "insira seu cpf (apenas números): ").strip())
        senha = input("Insira sua senha: ").strip()

        for i, cliente_atual in enumerate(base_clientes):
            if cliente_atual.cpf == cpf and cliente_atual.senha == senha:
                conta_selecionada = input(
                                    "Selecione uma conta: \n"
                                    f"{Conta.listar_contas(cpf)}\n\n"
                                    "=>"
                                    )
                return (True,
                        base_clientes.index(cliente_atual),
                        conta_selecionada)
        return None


@dataclass
class Conta:
    cpf: int
    cesta: int
    limite_saque_qtd: int
    limite_saque_valor: int
    tarifa: int
    conta: int
    numero_saques: int
    saldo: float
    agencia: str
    extrato: List[str] = field(default_factory=list)

    @staticmethod
    def deposito(saldo_cliente, extrato_cliente: list):

        data_hora = datetime.now()
        data = data_hora.strftime("%d/%m/%Y")
        hora = data_hora.strftime("%H:%M")

        valor = int(input("informe o valor do depósito"))

        if valor > 0:
            saldo_cliente += valor
            extrato_cliente.append(
                {"Deposito": valor, "Data": data, "Hora": hora}
            )
        else:
            print("Operação falhou! O valor informado é inválido.")
        return saldo_cliente, extrato_cliente

    @staticmethod
    def saque(saldo_cliente, extrato_cliente: list, numero_saques_cliente):

        data_hora = datetime.now()
        data = data_hora.strftime("%d/%m/%Y")
        hora = data_hora.strftime("%H:%M")

        valor = float(input("Informe o valor do saque: "))

        if valor > saldo_cliente:
            print("A operação falhou!"
                  " Saldo insuficiente.")
        elif valor > conta_acessada.limite_saque_valor:
            print("Operação falhou!"
                  " Limite de saque atingido.")
        elif numero_saques_cliente >= conta_acessada.limite_saque_qtd:
            print("Operação falhou!"
                  " Você atingiu o limite de saques da sua conta!")
        elif valor > 0:
            saldo_cliente -= valor
            extrato_cliente.append(
                {"Saque": valor, "Data": data, "Hora": hora}
            )
            numero_saques_cliente += 1
        else:
            print("Operação falhou!"
                  " O valor informado é inválido.")

        return saldo_cliente, extrato_cliente, numero_saques_cliente

    @staticmethod
    def alterar_cesta():

        opcao_cesta = {}

        while True:
            plano = input(
                "Selecione o tipo de plano desejado: \n\n"
                "[1] Prata:"
                " 3 saques, 2000 limite de saque, R$ 10.00.\n"
                "[2] Ouro:"
                " 5 saques, 5000 limite de saque, R$ 15.00.\n"
                "[3] Diamante:"
                " 10 saques, 10000 limite de saque, R$ 20.00.\n\n"
                "=>"
            )

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

    @staticmethod
    def formatar_extrato(extrato_cliente):

        saida = ""

        for lancamento in extrato_cliente:

            natureza = lancamento.get("Deposito")

            if natureza is None:
                saida += (f"Horário: {lancamento['Data']} |"
                          f" {lancamento['Hora']} |"
                          f"   Saque    |"
                          f" Valor: {lancamento['Saque']}\n")
            else:
                saida += (f"Horário: {lancamento['Data']} |"
                          f" {lancamento['Hora']} |"
                          f"  Deposito  |"
                          f" Valor: {lancamento['Deposito']}\n")

        return saida

    @staticmethod
    def mostrar_extrato(extrato_cliente, saldo_cliente):

        extrato_cliente = Conta.formatar_extrato(extrato_cliente)
        print("\n================ EXTRATO ================")
        print("\nSeu extrato está disponível, "
              f"{base_clientes[id_cliente].nome},"
              f" confira suas informações!")
        print(f"\nO plano selecionado foi: {conta_acessada.cesta}")
        print(f"\nDébito cesta de serviços R$ {conta_acessada.tarifa}")
        print(
            "Não foram realizadas movimentações."
            if not extrato_cliente
            else extrato_cliente
        )
        print(f"\nSaldo: R$ {(saldo_cliente - conta_acessada.tarifa):.2f}")
        print("===========================================")

    @staticmethod
    def listar_contas(cpf):
        mostrar_contas = ""

        for i in range(0, len(cliente_contas[cpf])):
            ag = cliente_contas[cpf][i].agencia
            cc = cliente_contas[cpf][i].conta
            mostrar_contas += (f"\n{[i + 1]} Agência: {ag},"
                               f" Conta corrente: {cc}")

        return mostrar_contas

    @staticmethod
    def cadastrar_conta(cpf_usuario):

        opcao_cesta = Conta.alterar_cesta()

        cesta_selecionada = opcao_cesta["Cesta selecionada"]
        limite_saque_qtd = opcao_cesta["Limite de saques quantidade"]
        limite_saque_valor = opcao_cesta["Limite de saques valor"]
        tarifa_selecionada = opcao_cesta["Tarifa"]

        if not cliente_contas:
            conta_gerada = 1
        else:
            conta_gerada = len(cliente_contas) + 1

        conta_usuario = conta_gerada

        return Conta(
            cpf=cpf_usuario,
            cesta=cesta_selecionada,
            limite_saque_qtd=limite_saque_qtd,
            limite_saque_valor=limite_saque_valor,
            tarifa=tarifa_selecionada,
            saldo=0,
            numero_saques=0,
            extrato=[],
            agencia="0001",
            conta=conta_usuario,
        )


base_clientes = []
cliente_contas = defaultdict(list)

while True:

    menu = input("""
    Escolha a opção desejada:
    [1] Entrar
    [2] Cadastrar-se
    [0] Sair
    => """)

    if menu == "1":

        try:
            resultado_login, id_cliente, conta_usada = Cliente.login_cliente()
        except TypeError:
            print("CPF ou senha incorretos, tente novamente.")
            continue

        conta_acessada = cliente_contas[base_clientes[id_cliente].cpf][
            int(conta_usada) - 1
        ]

        while resultado_login:

            opcao = input(
                f"Bem vindo {base_clientes[id_cliente].nome}\n"
                f"conta: {conta_acessada.conta}!\n"
                "Escolha o que deseja fazer:\n\n"
                "[1] Depositar\n"
                "[2] Sacar\n"
                "[3] Extrato\n"
                "[4] Alterar plano\n"
                "[5] Criar nova conta\n"
                "[6] Alterar conta\n"
                "[0] Sair\n\n"
                "=>"
            )

            if opcao == "1":
                conta_acessada.saldo, conta_acessada.extrato = Conta.deposito(
                    conta_acessada.saldo, conta_acessada.extrato
                )
            elif opcao == "2":
                (
                    conta_acessada.saldo,
                    conta_acessada.extrato,
                    conta_acessada.numero_saques,
                ) = Conta.saque(
                    conta_acessada.saldo,
                    conta_acessada.extrato,
                    conta_acessada.numero_saques,
                )
            elif opcao == "3":
                Conta.mostrar_extrato(
                    conta_acessada.extrato, conta_acessada.saldo
                )
            elif opcao == "4":
                dados_cesta = Conta.alterar_cesta()
            elif opcao == "5":
                nova_conta = Conta.cadastrar_conta(
                    base_clientes[id_cliente].cpf
                )
                cliente_contas[
                    base_clientes[id_cliente].cpf
                ].append(nova_conta)
                print(
                    f"Conta criada, Agencia: {nova_conta.agencia}"
                    f" Conta: {nova_conta.conta}"
                )

            elif opcao == "6":
                conta_usada = input(
                                "Selecione uma conta:\n"
                                f"{Conta.listar_contas(
                                    base_clientes[id_cliente].cpf
                                )}\n"
                                "=>"
                              )
            elif opcao == "0":
                exit()
            else:
                print("por favor, selecione uma opção válida")
        else:
            print("Login falhou, tente novamente!")

    if menu == "2":

        cliente, conta = Cliente.novo_cliente()
        base_clientes.append(cliente)
        cliente_contas.setdefault(cliente.cpf, []).append(conta)

    if menu == "0":
        exit()
