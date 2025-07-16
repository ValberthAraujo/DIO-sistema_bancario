import base_dados
from Modulos.Contas import Conta
from Modulos.Clientes import Cliente


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

            entrada_usuario = input(
                f"""
                Bem vindo {cliente.nome}!
                Escolha a conta que deseja acessar.
                
                {cliente.listar_contas()}
                """
            )
            
            conta_dados = cliente.escolher_conta(entrada_usuario)
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

            entrada_conta = input(
                f"Bem vindo {cliente.nome}\n"
                f"conta: {conta.conta}!\n"
                "Escolha o que deseja fazer:\n\n"
                "[1] Depositar\n"
                "[2] Sacar\n"
                "[3] Extrato\n"
                "[4] Mudar cesta de serviços\n"
                "[0] Sair\n\n"
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
            else:
                print("por favor, selecione uma opção válida")

    if menu == "2":
        Cliente.cadastrar_cliente()

    if menu == "0":
        exit()
