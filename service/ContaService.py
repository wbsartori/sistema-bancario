from model import conta
from db import db

class ContaService():

    def criar(self, dados):

        retornoCriar = db.DB.insert(db.DB, 'conta', dados)
        return retornoCriar

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