from model import conta
from db import db

class ContaService():

    def criar(self, id,titular,agencia,numeroConta,tipo,saldo):

        retornoCriar = db.DB.insert(db.DB, 'conta', ['conta', id, titular, agencia, numeroConta, tipo, saldo])

        if retornoCriar:
            retornoCriar()
        else:
            return False

    def listar(self):
        pass

    def alterar(self):
        pass

    def excluir(self):
        pass

    def sacar(self):
        pass

    def depositar(self):
        pass

    def transferir(self):
        pass

    def saldo(self):
        pass