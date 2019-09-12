from models import pessoa

class PessoaFisica(pessoa.Pessoa):
    def __init__(self,telefone, endereco, cidade, cpf, nome, dataNascimento):
        super().__init__(telefone, endereco, cidade)
        self.cpf = cpf
        self.nome = nome
        self.dataNascimento = dataNascimento

    def setCpf(self, cpf):
        self.cpf = cpf

    def setNome(self, nome):
        self.nome = nome

    def setDataNascimento(self, dataNascimento):
        self.dataNascimento = dataNascimento

    def getCpf(self):
        return self.cpf

    def getNome(self):
        return self.nome

    def getDataNascimento(self):
        return self.dataNascimento



