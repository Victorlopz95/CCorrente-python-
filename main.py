#Código feito por: Victor Lopes

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
            time.append(datetime.now().strftime('%d/%m/%y %H:%M:%S'))
            ext.append(dep)
            menu()
        elif opcao == 2:
            saq = float(input("Digite o valor do saque: "))
            if saq <= saldo:
                cont = cont + 1
                saldo = saque(saldo, saq)
                time.append(datetime.now().strftime('%d/%m/%y %H:%M:%S'))
                selecao.append(opcao)
                ext.append(saq)
                menu()
            else:
                print("Saldo insuficiente")
                menu()
        elif opcao == 3:
            extrato(cont, time, ext, selecao)
            menu()
        elif opcao == 4:
            consulta(saldo)
            menu()
        elif opcao == 5:
            print("F I M  D O  P R O G R A M A !")
        else:
            print("Opção inválida")
    except NameError:
        print("Opção inválida")
