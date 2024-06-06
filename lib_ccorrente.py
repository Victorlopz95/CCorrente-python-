def menu():
    print(">>>GESTÃO DE CONTA CORRENTE<<<")
    print("******************************")
    print("**   1) Depósito na Conta   **")
    print("**   2) Saque da Conta      **")
    print("**   3) Extrato da Conta    **")
    print("**   4) Saldo da Conta      **")
    print("**   5) Sair                **")
    print("******************************")


def deposito(saldo, dep):
    print("\nDepósito de R$", format(dep, '.2f'), "efeituado com sucesso")
    return saldo+dep


def saque(saldo, saq):
    if saldo < saq:
        print("\nSaldo insuficiente")
    else:
        print("\nSaque de R$", format(saq, '.2f'), "efeituado com sucesso")
    return saldo-saq


def extrato(cont, time, ext, selecao):
    for i in range(cont):
        if selecao[i] == 1:
            print("Depósito de R$", format(ext[i], '.2f'), "efetuado em:", time[i])
        elif selecao[i] == 2:
            print("Saque de R$", format(ext[i], '.2f'), "efetuado em:", time[i])
    return


def consulta(saldo):
    print("Seu saldo é de R$", format(saldo, '.2f'),".")
    return
