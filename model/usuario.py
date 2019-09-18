class Usuario:
    def __init__(self,id, usuario, senha, status):
        self.id = id
        self.usuario = usuario
        self.senha = senha
        self.status = status

    def setId(self, id):
        self.id = id

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setSenha(self, senha):
        self.senha = senha

    def setStatus(self, status):
        self.status = status

    def getId(self, id):
        return self.id

    def getUsuario(self, usuario):
        return self.usuario

    def getSenha(self, senha):
        return self.senha

    def getStatus(self, status):
        return self.status