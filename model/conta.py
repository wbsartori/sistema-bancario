class Conta:
    def __init__(self, id,id_usuario, titular,numeroConta, agencia, tipo, saldo):
        self.id = id
        self.id_usuario = id_usuario
        self.titular = titular
        self.agencia = agencia
        self.numeroConta = numeroConta
        self.tipo = tipo
        self.saldo = saldo

    def setId(self, id):
        self.id = id

    def setIdUsuario(self, id_usuario):
        self.id_usuario = id_usuario

    def setTitular(self, titular):
        self.titular = titular

    def setAgencia(self, agencia):
        self.agencia = agencia

    def setNumeroConta(self, numeroConta):
        self.numeroConta = numeroConta

    def setTipo(self, tipo):
        self.tipo = tipo

    def getId(self, id):
        return self.id

    def getIdUsuario(self, id_usuario):
        return self.id_usuario

    def getTitular(self, titular):
        return self.titular

    def getAgencia(self, agencia):
        return self.agencia

    def getNumeroConta(self, numeroConta):
        return self.numeroConta

    def getTipo(self, tipo):
        return self.tipo