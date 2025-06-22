menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>
"""

saldo = 0
limite = 500
extrato = ""
num_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do deposito"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operacao falhou! O valor informado eh invalido.")
    
    elif opcao == "2":
        valor = float(input("Informe o valor de saque"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = num_saques >= limite_saques

        if excedeu_saldo:
            print("Operacao falhou! Voce nao tem saldo suficiente.")
        elif excedeu_limite:
            print("Operacao falhou! O valor do saque excede o limite")
        elif excedeu_saques:
            print("Operacao falhou! O numero maximo de saque excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            num_saques += 1
        else: 
            print("Operacao falhou! O valor informado eh invalido.")
    
    elif opcao == "3":
        print("\n ==========EXTRATO===========")
        print("Nao foram realizados movimentacoes." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("\n ============================")

    elif opcao == "4":
        break

    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada")
