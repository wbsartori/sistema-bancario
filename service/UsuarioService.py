import hashlib
import sys

from model import usuario

from model import usuario
from db import db

class UsuarioService():

    def criar(self):
        pass

    def listar(self):
        pass

    def alterar(self):
        pass

    def excluir(self):
        pass

    def efetuarLogin(self, usuario, senha):
        if (usuario and senha):
            senha_criptografada = self.encryptSenha(self, senha.encode('utf-8'))

            retornoConsultaUsuario = db.DB.select(db.DB, 'usuario', ['usuario', usuario])
            retornoConsultaSenha = db.DB.select(db.DB, 'usuario', ['senha', senha_criptografada])

            # Retorna true ou false se encontrou um registro no arquivo pesquisando
            # pelo atributo "usuario" e "senha"
            if retornoConsultaUsuario and retornoConsultaSenha:
                return retornoConsultaUsuario
            else:
                return False


    def encryptSenha(self, senha):
        hash = hashlib.sha256()
        hash.update(senha)

        return hash.hexdigest()

