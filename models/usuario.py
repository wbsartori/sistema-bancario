class Usuario:
    def __init__(self, usuario, senha, status):
        self.usuario = usuario
        self.senha = senha
        self.status = status

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setSenha(self, senha):
        self.senha = senha

    def setStatus(self, status):
        self.status = status

    def getUsuario(self, usuario):
        return self.usuario

    def getSenha(self, senha):
        return self.senha

    def getStatus(self, status):
        return self.status