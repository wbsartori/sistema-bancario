#Importa as libs
import platform #Lib que reconhece o sistema operacional
import os       #Lib que possui recursos do sistema operacional
import sys
import time
from pyfiglet import Figlet #Lib para criar interface mais elaborada


#Função para limpar console de acordo com sistema operacional
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

while 1:
    clear()
    result = Figlet(font='doom')
    print(result.renderText('LadroBank'))
    print(' # Operações #')

    menuPrincipal = [' Sacar',' Depositar',' Transferir',' Saldo',' Sair']
    items = 1
    for mp in menuPrincipal:
        print( str(items) + ' - ' + mp)
        items = items + 1

    print('')
    opcoesPrincipal = int(input('Seleciona a operação: '))


    if opcoesPrincipal == 1:
        clear()
        ms = Figlet(font='doom')
        print(ms.renderText('Saque Bancário'))
        print(' # Operações #')

        menuSacar = ['Inserir Valor',' Voltar']
        items = 1
        for mSacar in menuSacar:
            print(str(items) + ' - ' + mSacar)
            items = items + 1

        saqueOP =  int(input('Operação: '))
        if saqueOP == 1:
            saque = int(input('Valor a sacar: '))
        else:
            break

    elif opcoesPrincipal == 2:
        print('Depositar')
        break
    elif opcoesPrincipal == 3:
        print('Transferir')
        break
    elif opcoesPrincipal == 4:
        print('Saldo')
        break
    elif opcoesPrincipal == 5:
        print('Obrigado por utilizar nossos serviços!')
        print('...' + time.sleep(1) + str('...') + time.sleep(1) + str('...') + time.sleep(1))
        break

    else:
        print('Operação não existe, tente novamente!')
        print('...')
        print('...')
        print('...')
        clear()
