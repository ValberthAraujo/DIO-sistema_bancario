import base_dados
from datetime import datetime
from decimal import Decimal

class Conta:

    def __init__(
            self,
            cpf: int,
            conta: int,
            numero_saque: int = 0,
            saldo: Decimal = Decimal("0.00"),
            cesta: str = "Prata",
            tarifa: int = 10,
            limite_saque: int = 3,
            agencia: int = 1
    ):

        # inseridos no init
        self.cpf = cpf
        self.conta = conta

        # protegidos
        self._numero_saque = numero_saque
        self._saldo = saldo

        # alterado posteriormente, esse é o Default
        self.cesta = cesta
        self.tarifa = tarifa
        self.limite_saque = limite_saque
        self.agencia = agencia

    def __repr__(self):
        print(f"Ação envolvendo o cpf {self.cpf}, de conta {self.conta}")

    def deposito(self) -> None:

        data_valor = datetime.now()
        data_texto = data_valor.strftime("%d/%m/%Y %H %M")

        valor = input("informe o valor do depósito").strip()
        valor = Decimal(valor)

        if valor > 0:
            self._saldo += valor
            base_dados.inserir_dados_extrato(self.conta, data_texto, "Deposito", valor)
        else:
            print("Operação falhou! O valor informado é inválido.")

    def saque(self) -> None:

        data_valor = datetime.now()
        data_texto = data_valor.strftime("%d/%m/%Y %H %M")

        valor = input("Informe o valor do saque: ")
        valor = Decimal(valor)

        if valor > self._saldo:
            print("A operação falhou!"
                  " Saldo insuficiente.")
        elif self._numero_saque >= self.limite_saque:
            print("Operação falhou!"
                  " Você atingiu o limite de saques da sua conta!")
        elif valor > 0:
            self._saldo -= valor
            self._numero_saque += 1
            base_dados.inserir_dados_extrato(self.conta, data_texto, "Saque", valor)
        else:
            print("Operação falhou!"
                  " O valor informado é inválido.")

    def alterar_cesta(self) -> None:

        while True:
            plano = input("""
            Selecione o tipo de plano desejado:

            [1] Prata: 3 saques, R$ 10.00.
            [2] Ouro: 5 saques, R$ 15.00.
            [3] Diamante: 10 saques, R$ 20.00.

            =>""")

            match plano:
                case "1":
                    self.cesta = "Prata"
                    self.limite_saque = 3
                    self.tarifa = 10
                case "2":
                    self.cesta = "Ouro"
                    self.limite_saque = 5
                    self.tarifa = 15
                case "3":
                    self.cesta = "Diamante"
                    self.limite_saque = 10
                    self.tarifa = 20
                case _:
                    print("Por favor, selecione uma opção válida")

    def mostrar_extrato(self) -> None:

        print("\n================ EXTRATO ================")
        print(f"\nO plano selecionado foi: {self.cesta}")
        print(f"\nDébito cesta de serviços R$ {self.tarifa}")
        base_dados.mostrar_extrato(self.conta)
        print(f"\nSaldo: R$ {(self._saldo - self.tarifa):.2f}")
        print("===========================================")

def cadastrar_conta(cpf: int):

    id_usuario = base_dados.id_usuario(cpf)

    base_dados.inserir_dados_contas(
        agencia=1,
        usuario_id=id_usuario,
        limite_saque=3,
        saldo=0,
        numero_saques=0,
        tarifa=10,
        cesta="Prata"
    )