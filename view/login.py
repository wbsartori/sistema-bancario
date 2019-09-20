# coding=utf-8
#Importa as libs
import platform #Lib que reconhece o sistema operacional
import os       #Lib que possui recursos do sistema operacional
import sys
import time
from pyfiglet import Figlet #Lib para criar interface mais elaborada
from view import operacoes
from getpass import getpass
from service import UsuarioService
import hashlib

class Login():

    def __init__(self):
        self.menu()

    #Função para limpar console de acordo com sistema operacional
    def clear(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def menu(self):
        while 1:
            self.clear()
            result = Figlet(font='doom')
            print(result.renderText('LadroBank'))
            print('# Acesso ao LadroBank #')
            print('')
            menuPrincipal = ['Entrar', 'Sair']
            items = 1
            for mp in menuPrincipal:
                print(str(items) + ' - ' + mp)
                items = items + 1
            print('')
            opcoesPrincipal = int(input('Selecione a operação: '))
            print('')
            if opcoesPrincipal == 1:
                self.clear()
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
                    senhaOP = getpass('Senha: (Ela não aparecerá na tela enquanto digita)')
                print('')

                # Instância o nosso serviço de usuário, onde tem todas as funções relacionadas
                # a usuários
                usuarioService = UsuarioService.UsuarioService

                # Atribui o retorno da função que verifica o usuário e senha, retorna o Usuário
                # caso o login esteja correto, e falso caso o contrário
                response = usuarioService.efetuarLogin(usuarioService, loginOP, senhaOP)

                # Se o login foi válido, chama a view de operações do usuário
                # Se não é renderizado o menu novamente na tela
                if response:
                    operacoes.Operacoes().menu(response['id'])
                else:
                    self.menu()

            elif opcoesPrincipal == 2:
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