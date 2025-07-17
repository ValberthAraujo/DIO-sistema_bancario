from typing import Optional
import base_dados

class Cliente:

    def __init__(self,
                 cpf: int,
                 nome: str,
                 senha: Optional[str] = None,
                 nascimento: Optional[int] = None,
                 endereco: Optional[str] = None
                 ):

        self.cpf = cpf
        self.nome = nome
        self._senha = senha
        self.nascimento = nascimento
        self.endereco = endereco

    def listar_contas(self) -> str:

        contas = base_dados.mostrar_contas(self.cpf)
        resultado = []

        for conta in contas:
            resultado.append(f"Conta [{conta[0]}]  |  saldo {conta[3]}.")

        return "\n".join(resultado)


    def escolher_conta(self, conta_selecionada):

        contas = base_dados.mostrar_contas(self.cpf)
        for conta in contas:
            if conta_selecionada == conta[0]:
                return conta
        return None

    @staticmethod
    def apagar_conta(saldo: int, conta: int) -> None:
        if saldo > 0:
            print("Não é possivel apagar a conta,"
                  "retire o saldo e tente novamente!")
        else:
            base_dados.apagar_conta(conta)
            print("Conta apagada com sucesso!")

    @staticmethod
    def cadastrar_conta(cpf: int) -> None:

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

    @staticmethod
    def cadastrar_cliente() -> None:

        # Inserção de dados
        nome = input("Insira seu nome: ").strip()
        senha = input("Informe a senha desejada: ").strip()
        cpf = input("Insira o seu CPF "
                    "(apenas números, 11 digitos) ").strip()
        data_nascimento = input("Digite a data de nascimento (DD/MM/YYYY)").strip()


        # Validação dos dados
        if len(cpf) != 11:
            print("Digite o cpf corretamente")
            return None

        cpf = int(cpf)

        if len(data_nascimento) == 10:
            data_nascimento = f"{data_nascimento[6:]}-{data_nascimento[3:5]}-{data_nascimento[0:2]}"
        elif len(data_nascimento) == 8:
            data_nascimento = f"{data_nascimento[4:]}-{data_nascimento[2:4]}-{data_nascimento[0:2]}"
        else:
            print("Por favor, digite a data de nascimento corretamente.")
            return None

        while True:

            logradouro = input("Informe seu logradoro: ").strip()
            bairro = input("Informe seu bairro: ").strip()
            cidade = input("Informe sua cidade: ").strip()
            estado = input("Informe seu estado: ").strip()

            endereco = f"{logradouro}, {bairro} - {cidade}/{estado}"

            resposta = input(
                "O endereço:\n"
                f"{endereco}\n"
                "está correto?\n\n"
                "[1] Sim\n"
                "[2] Não\n\n"
                "=> "
            )

            if resposta == "1":
                break
            else:
                continue

        base_dados.cadastrar_cliente(
            cpf,
            nome,
            senha,
            data_nascimento,
            endereco
        )

        Cliente.cadastrar_conta(cpf)

        return None