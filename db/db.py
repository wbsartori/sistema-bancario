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

        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, tabela + '.json')

        return filename

    def select(self, tabela, where):

        filename = self.getJSON(self, tabela)

        with open(filename) as file:
            banco = json.load(file)

            if len(where) == 0:
                return banco[tabela]
            elif len(where) == 2:

                for usuario in banco[tabela]:

                    if usuario[where[0]] == where[1]:
                        return usuario

    def delete(self, tabela, campo, valor):
        filename = self.getJSON(self, tabela)

        with open(filename) as file:
            banco = json.load(file)

            length = len(banco[tabela])

            for usuario in range(length):

                if banco[tabela][usuario][campo] == str(valor):
                    del banco[tabela][usuario]

            with open(filename, 'w') as file:
                json.dump(banco, file)

    def edit(self, tabela, where, valores):
        pass