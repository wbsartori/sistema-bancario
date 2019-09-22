#Importa as libs
import platform #Lib que reconhece o sistema operacional
import os       #Lib que possui recursos do sistema operacional
import sys
import time
from pyfiglet import Figlet #Lib para criar interface mais elaborada


from service import ContaService

class Cadastros():
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
            print(result.renderText('ADMIN'))
            print('# Cadastro de Clientes #')
            print('')
            menuPrincipal = [' Novo',' Lista',' Editar',' Excluir',' Sair']
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
                print(ms.renderText('Novo Cliente'))
                print('# Novo Cliente #')
                print('')
                menuNovo = ['Criar','Menu Principal']
                items = 1
                for mNovo in menuNovo:
                    print(str(items) + ' - ' + mNovo)
                    items = items + 1
                print('')
                novoOP = int(input('Operação: '))
                print('')
                if novoOP == 1:
                    print('Inserir os dados')
                    id          = input('ID: ')
                    titular     = input('Titular: ')
                    agencia     = input('Agencia: ')
                    numeroConta = input('Numero da Conta: ')
                    tipo        = input('Tipo: ')
                    saldo       = input('Saldo: ')

                    contaService = ContaService.ContaService
                    response = contaService.criar(contaService, id, titular,agencia,numeroConta,tipo,saldo)

                    if response:
                        print('Usuário Cadastrado com Sucesso!')
                        time.sleep(0.5)
                    else:
                        print('Erro ao cadastrar usuario !')
                        time.sleep(0.2)
                else:
                    print('Finalizando cadastro.')
                    time.sleep(1)
                    print('Obrigado por utilizar nossos serviços.')
                    time.sleep(0.8)

            elif opcoesPrincipal == 2:
                self.clear()
                ms = Figlet(font='doom')
                print(ms.renderText('Lista de Clientes'))
                print('# Lista de Clientes #')
                print('')
                menuListar = ['Listar', 'Menu Principal']
                items = 1
                for mListar in menuListar:
                    print(str(items) + ' - ' + mListar)
                    items = items + 1
                print('')
                listarOP = int(input('Operação: '))
                print('')
                if listarOP == 1:
                    print('Lista de Clientes')
                else:
                    print('Finalizando Operação de Listagem.')
                    time.sleep(1)
                    print('Obrigado por utilizar nossos serviços.')
                    time.sleep(0.8)

            elif opcoesPrincipal == 3:
                self.clear()
                ms = Figlet(font='doom')
                print(ms.renderText('Editar Cadastro'))
                print('# Editar Cadastro #')
                print('')
                menuEditar = ['Editar', 'Menu Principal']
                items = 1
                for mEditar in menuEditar:
                    print(str(items) + ' - ' + mEditar)
                    items = items + 1
                print('')
                editarOP = int(input('Operação: '))
                print('')
                if editarOP == 1:
                    print('Editar Cliente.')
                else:
                    print('Finalizando Operação de Edição.')
                    time.sleep(1)
                    print('Obrigado por utilizar nossos serviços.')
                    time.sleep(0.8)

            elif opcoesPrincipal == 4:
                self.clear()
                ms = Figlet(font='doom')
                print(ms.renderText('Excluir Cliente'))
                print(' # Excluir Cliente #')
                print('')
                menuExcluir = ['Excluir', 'Menu Principal']
                items = 1
                for mExcluir in menuExcluir:
                    print(str(items) + ' - ' + mExcluir)
                    items = items + 1
                print('')
                excluirOP = int(input('Operação: '))
                print('')
                if excluirOP == 1:
                    print('Excluindo Cliente')
                    time.sleep(1)
                else:
                    print('Finalizando Operação de Exclusão.')
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
