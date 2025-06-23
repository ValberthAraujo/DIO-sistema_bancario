# Global

menu = """

Bem vindo! Escolha o que deseja fazer.

[1] Depositar
[2] Sacar
[3] Extrato
[4] Alterar plano
[0] Sair

=> """

cesta_servicos = """

Selecione o tipo de plano desejado:

[1] Prata: 3 saques, R$ 10.00
[2] Ouro: 5 saques, R$ 15.00
[3] Diamante: 10 saques, R$ 20.00

"""

cestas_disponiveis = ["Prata", "Ouro", "Diamante"]

# Clientes
plano = "1"
saldo = 0
limite = 500
extrato = ""
limite_saque = 3
tarifa = 10


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        
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

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print(f"\nO plano selecionado foi: {cestas_disponiveis[int(plano) - 1]}")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {(saldo - tarifa):.2f}")
        print("==========================================")

    elif opcao == "4":
        plano = input(cesta_servicos)

        match plano:

            case "1":
                limite_saque = 3
                tarifa = 10
                if numero_saques >= limite_saque:
                    print("Plano excedido, escolha outro plano")
                    exit()
            case "2":
                limite_saque = 5
                tarifa = 
                if numero_saques >= limite_saque:
                    print("Plano excedido, escolha outro plano")
                    exit()
            case "3":
                limite_saque = 10
                tarifa = 20
                if numero_saques >= limite_saque:
                    print("Plano excedido, escolha outro plano")
                    exit()
            case _:
                print("Por favor, selecionar um dos números")
                exit()
        

    elif opcao == "0":
