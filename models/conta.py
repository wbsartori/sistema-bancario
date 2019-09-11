class Conta:
    def __init__(self, codigo, titular,numeroConta, agencia, tipo, saldo):
        self.codigo = codigo
        self.titular = titular
        self.agencia = agencia
        self.numeroConta = numeroConta
        self.tipo = tipo
        self.saldo = saldo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setTitular(self, titular):
        self.titular = titular

    def setAgencia(self, agencia):
        self.agencia = agencia

    def setNumeroConta(self, numeroConta):
        self.numeroConta = numeroConta

    def setTipo(self, tipo):
        self.tipo = tipo

    def getCodigo(self, codigo):
        return self.codigo

    def getTitular(self, titular):
        return self.titular

    def getAgencia(self, agencia):
        return self.agencia

    def getNumeroConta(self, numeroConta):
        return self.numeroConta

    def getTipo(self, tipo):
        return self.tipo