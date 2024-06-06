from datetime import datetime
from lib_ccorrente import *

datahora = datetime.now().strftime('%d/%m/%y %H:%M:%S')
print(datahora)
opcao = 0
selecao = []
time = []
ext = []
cont = 0
saldo = 0
menu()

while opcao < 5:
    try:
        opcao = eval(input("\nDigite o número de uma das opções acima: "))
        if opcao == 1:
            cont = cont+1
            dep = float(input("Digite o valor do depósito: "))
            saldo = deposito(saldo, dep)
            selecao.append(opcao)
            time.append(datahora)
            ext.append(dep)
            menu()
        elif opcao == 2:
            cont = cont + 1
            saq = float(input("Digite o valor do saque: "))
            saldo = saque(saldo, saq)
            selecao.append(opcao)
            time.append(datahora)
            ext.append(saq)
            menu()
        elif opcao == 3:
            extrato(cont, time, ext, selecao)
        elif opcao == 4:
            consulta(saldo)
        elif opcao == 5:
            print("F I M  D O  P R O G R A M A !")
        else:
            print("Opção inválida")
    except NameError:
        print("Opção inválida")
