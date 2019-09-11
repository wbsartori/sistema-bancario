from models import pessoa

class PessoaJuridica(pessoa.Pessoa):
    def __init__(self, telefone, endereco, cidade, cnpj, nomeFantasia, razaoSocial):
        super().__init__(telefone, endereco, cidade)
        self.cnpj = cnpj
        self.nomeFantasia = nomeFantasia
        self.razaoSocial = razaoSocial

    def setCnpj(self, cnpj):
        self.cnpj = cnpj

    def setNomeFantasia(self, nomeFantasia):
        self.nomeFantasia = nomeFantasia

    def setRazaoSocial(self, razaoSocial):
        self.razaoSocial = razaoSocial

    def getCnpj(self):
        return self.cnpj

    def getNomeFantasia(self):
        return self.nomeFantasia

    def getRazaoSocial(self):
        return self.razaoSocial

