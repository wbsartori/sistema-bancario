from models import conta
from models import pessoa
class ControllerConta(Pessoa, ContaCorrente, ContaPoupanca):
    def sacar(self, valor):
        pass

    def depositar(self,nAgencia, nConta, valor):
        pass

    def transferir(self, numeroConta, agencia, valor):
        pass
    