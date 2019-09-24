import sys
from db import db

class ContaService():

    # Cria uma conta para um usuário.
    def criar(self, dados):
        retornoCriar = db.DB.insert(db.DB, 'conta', dados)
        return retornoCriar

    # Função que realiza um saque de um usuário na sua conta.
    # É recebido por parâmetro o valor do saque, e o id do
    # logado que está fazendo o saque, para consultar a sua conta.
    def sacar(self, valorSaque, idUsuario):

        # Verifica se o valor solicitado pelo usuário é positivo
        if valorSaque > 0:
            # Se o id do usuário logado existe e veio corretamente
            if idUsuario:
                # Chama a classe manipuladora do banco e consulta o arquivo de contas
                # buscando pela chave "id_usuario" que é o usuário dono da conta, com base
                # no usuário que veio como parâmetro.
                conta = db.DB.select(db.DB, 'conta', ['id_usuario', idUsuario])

                # Se a conta existir
                if conta:
                    # Verifica se o saldo é maior que 0 e se o saldo é suficiente para sacar.
                    if int(conta['saldo']) > 0 and int(conta['saldo']) - int(valorSaque) >= 0:

                        # Pega o saldo atual da conta e diminui com o valor de saque.
                        novoSaldo = int(conta['saldo']) - int(valorSaque)
                        # Atualiza o objeto da conta com o novo saldo.
                        conta['saldo'] = str(novoSaldo)

                        # Chama a operação Edit da classe do banco, Onde é passado por parâmetro
                        # os novos dados atualizados da conta do usuário após o saque.
                        # ['id_usuario', idUsuario] serve para filtrar a conta do usuário
                        # que veio por parâmetro
                        db.DB.edit(db.DB, 'conta', ['id_usuario', idUsuario], conta)

                        return 'Saldo de R$' + str(valorSaque) + ' Realizado com Sucesso!'

                    else:
                        # Mensagem de erro
                        return 'Saldo Insuficiente!'
                else:
                    # Mensagem de erro
                    return 'Conta não encontrada!'
            else:
                # Mensagem de erro
                return 'Erro: ID do usuário inválido!'
        else:
            # Mensagem de erro
            return 'Erro: Valor negativo informado!'

    # Deposita um valor na conta do usuário
    def depositar(self, valor, idUsuario):
        # verifica se o valor é positivo
        if valor > 0:
            # Verifica se existe um usuário
            if idUsuario:

                # Pega a conta do usuário para realizar o saque
                conta = db.DB.select(db.DB, 'conta', ['id_usuario', idUsuario])

                # Se a conta existir
                if conta:

                    # Pega o saldo atual da conta e incrementa com o valor de depósito.
                    novoSaldo = int(conta['saldo']) + int(valor)
                    # Atualiza o objeto da conta com o novo saldo.
                    conta['saldo'] = str(novoSaldo)

                    # Chama a operação Edit da classe do banco, Onde é passado por parâmetro
                    # os novos dados atualizados da conta do usuário após o saque.
                    # ['id_usuario', idUsuario] serve para filtrar a conta do usuário
                    # que veio por parâmetro
                    db.DB.edit(db.DB, 'conta', ['id_usuario', idUsuario], conta)

                    return 'Depósito de R$' + str(valor) + ' Realizado com Sucesso!'
                else:
                    # Mensagem de erro
                    return 'Conta não encontrada!'
            else:
                # Mensagem de erro
                return 'Usuário inválido!'
        else:
            # Mensagem de erro
            return 'Erro: Valor negativo informado!'

    # Função que retorna o saldo em conta de um usuário
    def saldo(self, idUsuario):
        # Verifica se o usuário existe
        if idUsuario:
            # Chama a função select da classe de banco, buscando
            # pela chave "id_usuario", que é o id do usuário de qual a conta pertence.
            conta = db.DB.select(db.DB, 'conta', ['id_usuario', idUsuario])

            # Se encontrou uma conta retorna o saldo
            if conta:
                return 'Saldo Atual: R$' + conta['saldo']
            # Se não retorna um erro.
            else:
                # Mensagem de erro
                return 'Conta não encontrada!'
        else:
            # Mensagem de erro
            return 'Usuário inválido!'