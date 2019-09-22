# Biblioteca para criptografar a senha
import hashlib

# Classe DB para realizar operações no sistema de arquivos
from db import db

class UsuarioService():

    # Função que cria um novo usuário
    def criar(self, dados):

        # Verifica se os dados existem
        if dados:

            # Criptografa a senha inputada pelo usuário, e atribui para a mesma
            # posição do array de dados
            dados['senha'] = self.encryptSenha(self, dados['senha'].encode('utf-8'))

            # Chama a função insert da classe manipuladora do banco
            retornoCriar = db.DB.insert(db.DB, 'usuario', dados)
            return retornoCriar

    # Função que lista todos os registros do arquivo
    def listar(self):

        # Retorna a consulta select da classe que manipula o banco.
        return db.DB.select(db.DB, 'usuario', '')

    # Função para alterar um usuário.
    # São passados os novos dados por parâmetro, e um ID usado como referência
    # para saber qual usuário editar.
    def alterar(self, dados, id):

        # Criptografa a senha.
        dados['senha'] = self.encryptSenha(self, dados['senha'].encode('utf-8'))

        # Chama a função edit e retorna a resposta.
        retornoEditar = db.DB.edit(db.DB, 'usuario', ['id', id], dados)
        return retornoEditar

    # Excluí um usuário com base em um ID passado por parâmetro.
    def excluir(self, id):
        return db.DB.delete(db.DB, 'usuario', 'id', id)

    # Função que efetua login no sistema.
    def efetuarLogin(self, usuario, senha):

        # Se existir um usuário e uma senha
        if (usuario and senha):

            # Criptografa a senha para comparar.
            senha_criptografada = self.encryptSenha(self, senha.encode('utf-8'))

            # Faz uma consulta pelo usuário e depois pela senha.
            retornoConsultaUsuario = db.DB.select(db.DB, 'usuario', ['usuario', usuario])
            retornoConsultaSenha = db.DB.select(db.DB, 'usuario', ['senha', senha_criptografada])

            # Retorna true ou false se encontrou um registro no arquivo pesquisando
            # pelo atributo "usuario" e "senha"
            if retornoConsultaUsuario and retornoConsultaSenha:
                return retornoConsultaUsuario
            else:
                return False

    # Função que utiliza a lib "hashlib" para criptografar a senha.
    # É gerado um hash com base na string que vem como parâmetro.
    def encryptSenha(self, senha):
        hash = hashlib.sha256()
        hash.update(senha)

        return hash.hexdigest()

