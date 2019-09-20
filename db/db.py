import json
import sys
import os

class DB():

    USUARIO = './../db/usuario.json'
    CONTA = './../db/conta.json'

    def __init__(self):
        self.usuario = json.load(self.USUARIO)
        self.conta = json.load(self.CONTA)
        pass

    def getJSON(self, tabela):
        return tabela + '.json'

    def select(self, tabela, where):

        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, self.getJSON(self, tabela))

        with open(filename) as file:
            banco = json.load(file)

            if len(where) == 0:
                return banco[tabela]
            elif len(where) == 2:

                retorno = { }

                for usuario in banco[tabela]:

                    if usuario[where[0]] == where[1]:
                        retorno = usuario
                        return retorno
