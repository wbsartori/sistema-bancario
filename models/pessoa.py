class Pessoa:
    def __init__(self, telefone, endereco, cidade):
        self.telfone = telefone
        self.endereco = endereco
        self.cidade = cidade

    def setTelefone(self, telefone):
        self.telefone = telefone

    def setEndereco(self, endereco):
        self.endereco = endereco

    def setCidade(self, cidade):
        self.cidade = cidade

    def getTelefone(self):
        return self.telefone

    def getEndereco(self):
        return self.endereco

    def getCidade(self):
        return self.cidade