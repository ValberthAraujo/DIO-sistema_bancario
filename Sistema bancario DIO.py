import base_dados
from Clientes import Cliente
from Contas import Conta


while True:

    menu = input("""
    Escolha a opção desejada:
    [1] Entrar
    [2] Cadastrar-se
    [0] Sair
    => """)

    if menu == "1":

        cpf = int(input("Insira seu cpf! ").strip())
        senha = input("Insira sua senha! ").strip()

        usuario = base_dados.login(cpf, senha)

        exit() if usuario is None else usuario

        cliente = Cliente(usuario[1],usuario[2])

        while True:

            contas_disponiveis = cliente.listar_contas()

            entrada_usuario = input(
                f"Bem vindo {cliente.nome}!\n"
                "Escolha a conta que deseja acessar.\n"
                f"\n{contas_disponiveis}"
                "\n\n=>"
            )
            
            conta_dados = cliente.escolher_conta(int(entrada_usuario))
            conta = Conta(
                cpf=cliente.cpf,
                conta=conta_dados[0],
                numero_saque=conta_dados[5],
                saldo=conta_dados[3],
                cesta=conta_dados[7],
                tarifa=conta_dados[6],
                limite_saque=conta_dados[4],
                agencia=conta_dados[1]
            )

            tela_conta=True

            while tela_conta:
                entrada_conta = input(
                    f"Bem vindo {cliente.nome}\n"
                    f"conta: {conta.conta}!\n"
                    "Escolha o que deseja fazer:\n\n"
                    "[1] Depositar\n"
                    "[2] Sacar\n"
                    "[3] Extrato\n"
                    "[4] Mudar cesta de serviços\n"
                    "[5] Cadastrar nova conta!\n"
                    "[0] Voltar ao menu\n\n"
                    "=>"
                )

                if entrada_conta == "1":
                    conta.deposito()
                elif entrada_conta == "2":
                    conta.saque()
                elif entrada_conta == "3":
                    conta.mostrar_extrato()
                elif entrada_conta == "4":
                    conta.alterar_cesta()
                elif entrada_conta == "5":
                    conta.cadastrar_conta(cliente.cpf)
                    tela_conta = False
                elif entrada_conta == "0":
                    tela_conta = False
                else:
                    print("por favor, selecione uma opção válida")

    if menu == "2":
        Cliente.cadastrar_cliente()

    if menu == "0":
        exit()
