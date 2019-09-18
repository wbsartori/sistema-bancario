#Importa as libs
import platform #Lib que reconhece o sistema operacional
import os       #Lib que possui recursos do sistema operacional
import sys
import time
from pyfiglet import Figlet #Lib para criar interface mais elaborada

class Login():
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
        print('# Acesso ao LadroBank #')
        print('')
        menuPrincipal = ['Entrar', 'Sair']
        items = 1
        for mp in menuPrincipal:
            print( str(items) + ' - ' + mp)
            items = items + 1
        print('')
        opcoesPrincipal = int(input('Selecione a operação: '))
        print('')
        if opcoesPrincipal == 1:
            clear()
            ms = Figlet(font='doom')
            print(ms.renderText('Entrar'))
            print('# Entrar no Sistema #')
            print('')
            print('Digite o usuário e senha ou Digite 2 para voltar ao menu principal..')
            print('')
            loginOP = str(input('Usuario: '))
            if loginOP == '2':
                print('...')
                time.sleep(1)
                print('Finalizando Login.')
                time.sleep(0.8)
            else:
                senhaOP = int(input('Senha: '))
            print('')


        elif opcoesPrincipal == 2:
            i = ' '
            print('')
            print('Finalizando Sistema', end='')
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
            clear()
