from models import conta

class ContaPoupanca(conta.Conta):
    def __init__(self,codigo, titular, agencia, numeroConta, tipo, saldo, percentAdicional):

        super().__init__(codigo, titular, agencia, numeroConta, tipo, saldo)
        self.pecentAdicional = percentAdicional

