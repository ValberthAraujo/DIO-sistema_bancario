from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Union, Dict


@dataclass
class Cliente:
    cpf: int
    nome: str
    _senha: str
    nascimento: int
    endereco: str

    def listar_contas(self):
        pass



@dataclass
class Conta(Cliente):
    cpf: int
    cesta: str
    limite_saque_qtd: int
    tarifa: int
    conta: int
    _numero_saques: int
    _saldo: float
    agencia: str
    _extrato: List[Dict[str, Union[str, int]]] = field(default_factory=list)

    def deposito(self):

        data_hora = datetime.now()
        data = data_hora.strftime("%d/%m/%Y")
        hora = data_hora.strftime("%H:%M")

        valor = int(input("informe o valor do depósito"))

        if valor > 0:
            self._saldo += valor
            self._extrato.append(
                {"Deposito": valor, "Data": data, "Hora": hora}
            )
        else:
            print("Operação falhou! O valor informado é inválido.")


    def saque(self):

        data_hora = datetime.now()
        data = data_hora.strftime("%d/%m/%Y")
        hora = data_hora.strftime("%H:%M")

        valor = float(input("Informe o valor do saque: "))

        if valor > self._saldo:
            print("A operação falhou!"
                  " Saldo insuficiente.")
        elif valor > conta_acessada.limite_saque_valor:
            print("Operação falhou!"
                  " Limite de saque atingido.")
        elif self._numero_saques >= conta_acessada.limite_saque_qtd:
            print("Operação falhou!"
                  " Você atingiu o limite de saques da sua conta!")
        elif valor > 0:
            self._saldo -= valor
            self._extrato.append(
                {"Saque": valor, "Data": data, "Hora": hora}
            )
            self._numero_saques += 1
        else:
            print("Operação falhou!"
                  " O valor informado é inválido.")

        return self._saldo, self._extrato, self._numero_saques

    def alterar_cesta(self):

        while True:
            plano = input(
                "Selecione o tipo de plano desejado: \n\n"
                "[1] Prata:"
                " 3 saques, R$ 10.00.\n"
                "[2] Ouro:"
                " 5 saques, R$ 15.00.\n"
                "[3] Diamante:"
                " 10 saques, R$ 20.00.\n\n"
                "=>"
            )

            match plano:
                case "1":
                    self.cesta = "Prata"
                    self.limite_saque_qtd = 3
                    self.tarifa = 10
                case "2":
                    self.cesta = "Ouro"
                    self.limite_saque_qtd = 5
                    self.tarifa = 15
                case "3":
                    self.cesta = "Diamante"
                    self.limite_saque_qtd = 10
                    self.tarifa = 20
                case _:
                    print("Por favor, selecione uma opção válida")

    def formatar_extrato(self):

        saida = ""

        for lancamento in self._extrato:

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

    def mostrar_extrato(self):

        if not self._extrato:
            print("Não foram realizadas movimentações")
            return
        else:
            print("\n================ EXTRATO ================")
            print("\nSeu extrato está disponível, "
                  f"{self.formatar_extrato()},"
                  f" confira suas informações!")
            print(f"\nO plano selecionado foi: {self.cesta}")
            print(f"\nDébito cesta de serviços R$ {self.tarifa}")
            print(f"\nSaldo: R$ {(self._saldo - self.tarifa):.2f}")
            print("===========================================")

    def cadastrar_conta(self, cpf_usuario):

        self.alterar_cesta()

        if not cliente_contas:
            conta_gerada = 1
        else:
            conta_gerada = len(cliente_contas) + 1

        conta_usuario = conta_gerada

        return Conta(
            cpf=cpf_usuario,
            _saldo=0,
            _numero_saques=0,
            agencia="0001",
            conta=conta_usuario,
            cesta=self.cesta,
            limite_saque_qtd=self.limite_saque_qtd,
            tarifa=self.tarifa,
            endereco=super().endereco,
            nascimento=super().nascimento,
            nome=super().nome,
            _senha="protected"
        )

def cadastrar_cliente():

    nome = input("Insira seu nome: ").strip()
    senha = input("Informe a senha desejada: ").strip()


    cpf_usuario = input("Insira o seu CPF "
                        "(apenas números, 11 digitos) ")

    if len(cpf_usuario) != 11:
        print("Digite o cpf corretamente")
        exit()

    cpf_usuario = int(cpf_usuario)

    data_nascimento = input("Digite a data de nascimento (DDMMYYYY)")

    if len(data_nascimento) != 8:
        print("Digite corretamente a data de nascimento")
        exit()

    data_nascimento = int(data_nascimento)

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
        nome=nome,
        _senha=senha,
        nascimento=data_nascimento,
        endereco=endereco_usuario,
    )

def login_cliente():
    cpf = int(input("Bem vindo cliente, "
                    "insira seu cpf (apenas números): ").strip())
    senha = input("Insira sua senha: ").strip()

    for i, cliente_atual in enumerate(base_clientes):
        if cliente_atual.cpf == cpf and cliente_atual.senha == senha:
            conta_selecionada = input(
                                "Selecione uma conta: \n"
                                f"{Cliente.listar_contas()}\n\n"
                                "=>"
                                )
            return (True,
                    base_clientes.index(cliente_atual),
                    conta_selecionada)
    return None


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
            resultado_login, id_cliente, conta_usada = login_cliente()
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
                conta_acessada.deposito()
            elif opcao == "2":
                conta_acessada.saque()
            elif opcao == "3":
                pass
            elif opcao == "4":
                conta_acessada.alterar_cesta()
            elif opcao == "5":
                pass

            elif opcao == "6":
                conta_usada = input(
                                "Selecione uma conta:\n"
                                f"{Cliente.listar_contas(
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
        cadastrar_cliente()
    if menu == "0":
        exit()
