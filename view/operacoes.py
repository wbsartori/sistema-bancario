#Importa as libs
import platform #Lib que reconhece o sistema operacional
import os       #Lib que possui recursos do sistema operacional
import sys
import time
from pyfiglet import Figlet #Lib para criar interface mais elaborada

class Operacoes():
    #Função para limpar console de acordo com sistema operacional
    def clear(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def menu(self, idUsuarioLogado):
        while 1:
            self.clear()
            result = Figlet(font='doom')
            print(result.renderText('LadroBank'))
            print('# Operações Disponíveis #')
            print('')
            menuPrincipal = [' Sacar',' Depositar',' Transferir',' Saldo',' Sair']
            items = 1
            for mp in menuPrincipal:
                print( str(items) + ' - ' + mp)
                items = items + 1
            print('')
            opcoesPrincipal = int(input('Selecione a operação: '))
            print('')
            if opcoesPrincipal == 1:
                self.clear()
                ms = Figlet(font='doom')
                print(ms.renderText('Saques'))
                print('# Operações Disponíveis #')
                print('')
                menuSacar = ['Sacar','Menu Principal']
                items = 1
                for mSacar in menuSacar:
                    print(str(items) + ' - ' + mSacar)
                    items = items + 1
                print('')
                saqueOP = int(input('Operação: '))
                print('')
                if saqueOP == 1:
                    saque = int(input('Valor a sacar: '))
                else:
                    print('Finalizando Operação de Saque.')
                    time.sleep(1)
                    print('Obrigado por utilizar nossos serviços.')
                    time.sleep(0.8)

            elif opcoesPrincipal == 2:
                self.clear()
                ms = Figlet(font='doom')
                print(ms.renderText('Depositos'))
                print('# Operações Disponíveis #')
                print('')
                menuDepositar = ['Depositar', 'Menu Principal']
                items = 1
                for mDeposito in menuDepositar:
                    print(str(items) + ' - ' + mDeposito)
                    items = items + 1
                print('')
                depositoOP = int(input('Operação: '))
                print('')
                if depositoOP == 1:
                    conta = int(input('Conta: '))
                    agencia = int(input('Agencia: '))
                    deposito = int(input('Valor a depositar: '))
                else:
                    print('Finalizando Operação de Depósito.')
                    time.sleep(1)
                    print('Obrigado por utilizar nossos serviços.')
                    time.sleep(0.8)

            elif opcoesPrincipal == 3:
                self.clear()
                ms = Figlet(font='doom')
                print(ms.renderText('Transferencias'))
                print('# Operações Disponíveis #')
                print('')
                menuTransferir = ['Transferir', 'Menu Principal']
                items = 1
                for mTransferir in menuTransferir:
                    print(str(items) + ' - ' + mTransferir)
                    items = items + 1
                print('')
                depositoOP = int(input('Operação: '))
                print('')
                if depositoOP == 1:
                    conta = int(input('Conta: '))
                    agencia = int(input('Agencia: '))
                    deposito = int(input('Valor a transferir: '))
                else:
                    print('Finalizando Operação de Transferência.')
                    time.sleep(1)
                    print('Obrigado por utilizar nossos serviços.')
                    time.sleep(0.8)


            elif opcoesPrincipal == 4:
                self.clear()
                ms = Figlet(font='doom')
                print(ms.renderText('Saldos'))
                print(' # Operações #')
                print('')
                menuSaldo = ['Ver Saldo', 'Menu Principal']
                items = 1
                for mSaldo in menuSaldo:
                    print(str(items) + ' - ' + mSaldo)
                    items = items + 1
                print('')
                depositoOP = int(input('Operação: '))
                print('')
                if depositoOP == 1:
                    print('Saldo = R$ 5000,00')
                    time.sleep(1)
                else:
                    print('Finalizando Operação de Saldo.')
                    time.sleep(1)
                    print('Obrigado por utilizar nossos serviços.')
                    time.sleep(0.8)

            elif opcoesPrincipal == 5:
                i = ' '
                print('')
                print('Finalizando Sistema', '')
                time.sleep(1)

                for p in range(5):
                    print(i)
                    time.sleep(0.5)

                print('Obrigado por utilizar nossos serviços.')
                print('')
                msg = Figlet(font='doom')
                print(msg.renderText('LadroBank Agradece !'))
                time.sleep(0.8)
                break

            else:
                print('Operação não existe, tente novamente!')
                time.sleep(1.5)
                self.clear()
