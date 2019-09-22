# Biblioteca para criptografar a senha
import hashlib

# Classe DB para realizar operações no sistema de arquivos
from db import db

class UsuarioService():

    def criar(self, dados):
        if dados:

            dados['senha'] = self.encryptSenha(self, dados['senha'].encode('utf-8'))

            retornoCriar = db.DB.insert(db.DB, 'usuario', dados)
            return retornoCriar

    def listar(self):
        return db.DB.select(db.DB, 'usuario', '')

    def alterar(self):
        pass

    def excluir(self, id):
        return db.DB.delete(db.DB, 'usuario', 'id', id)

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

