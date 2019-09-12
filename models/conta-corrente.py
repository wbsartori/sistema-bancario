from models import conta

class ContaCorrente(conta.Conta):
    def __init__(self,codigo, cliente, agencia, numeroConta, tipo, saldo, taxa):

        super().__init__(codigo, cliente, agencia, numeroConta, tipo, saldo)
        self.taxa = taxa

