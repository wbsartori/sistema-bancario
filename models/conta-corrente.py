from models import conta

class ContaCorrente(conta):
    def __init__(self,codigo, cliente, agencia, numeroConta, tipo, saldo):
        super().__init__(codigo, cliente, agencia, numeroConta, tipo, saldo)


