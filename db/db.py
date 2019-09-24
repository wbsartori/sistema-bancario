import json
import os

# Classe responsável por manipular o  nosso sistema
# de arquivos.
class DB():

    # Função que retorna o caminho do arquivo
    # com base no nome da tabela.
    #
    # Exemplo: Parâmetro = 'usuario'
    # Retorno: '/usuarioqualquer/sistema-bancario/db/usuario.json'
    def getJSON(self, tabela):

        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, tabela + '.json')

        return filename

    # Função que faz um "select" nos arquivos de banco.
    # Recebemos por parâmetro o nome da tabela (usuario ou conta)
    # que representa o nome do arquivo.
    #
    # O segundo parâmetro é uma implementação simples de um "where".
    # Caso venha vazio, é retornado todos os registros do arquivo
    # especificado. Caso contrário é aplicado um filtro.
    #
    # Exemplo de WHERE: ['id', '250']
    # Se a tabela for usuario, irá buscar um usuário que contenha
    # o campo 'id' com valor de '250'.
    def select(self, tabela, where):
        # Pega o nome do arquivo.
        filename = self.getJSON(self, tabela)

        # Abre o arquivo
        with open(filename) as file:
            # Carrega o conteúdo do arquivo em uma variável.
            banco = json.load(file)

            # Se não tiver where, retorna todos os registros.
            if len(where) == 0:
                return banco[tabela]
            # Se tiver um where
            elif len(where) == 2:
                # Percorre todos os itens do arquivo
                for usuario in banco[tabela]:

                    # Verifica pela chave e valor se algum registro bate
                    if usuario[where[0]] == where[1]:
                        # Se sim ele é retornado
                        return usuario
    # Função que realiza uma operação de "insert" no sistema de arquivos.
    # É recebido por parâmetro o nome de uma tabela, que seria o nome
    # do arquivo, e um objeto contendo os seus valores.
    def insert(self, tabela, valores):
        # Pega o nome do arquivo.
        filename = self.getJSON(self, tabela)
        # Abre o arquivo
        with open(filename) as file:
            # Carrega o arquivo em uma variável
            banco = json.load(file)
            # Verifica se existem valores
            if (valores):
                # Adiciona uma nova posição no array de dados
                # contendo os valores recebidos.
                banco[tabela].append(valores)
        # Abre o arquivo novamente com permissão de escrita.
        with open(filename, 'w') as file:
            # Salva o arquivo com os dados atualizados.
            json.dump(banco, file, indent=4)
        # Retorno
        return True

    # Operação para deletar um registro dos arquivos.
    # Recebemos por parâmetro o nome de uma tabela,
    # um campo para usar como referência de filtro, e
    # um valor para comparar.
    #
    # Exemplo: chave = 'id' valor = '4'
    # É buscado no arquivo um item com a chave 'id' que bata
    # com o valor '4' para sabermos qual registro deletar.
    def delete(self, tabela, campo, valor):
        # Pega o nome do arquivo.
        filename = self.getJSON(self, tabela)
        # Abre o arquivo
        with open(filename) as file:
            # Carrega o arquivo em uma variável
            banco = json.load(file)
            # Pega o tamanho do arquivo para usar em um laço.
            length = len(banco[tabela])
            # Para cada item existente
            for usuario in range(length):
                # Verifica se o campo bate com o valor
                if banco[tabela][usuario][campo] == str(valor):
                    # Se sim, deleta o item
                    del banco[tabela][usuario]
            # Abre o arquivo com permissão de escrita
            with open(filename, 'w') as file:
                # Salva o novo arquivo atualizado
                json.dump(banco, file, indent=4)
        # Retorno
        return True

    # Função para editar um registro nos arquivos.
    # Recebemos o nome de um arquivo por parâmetro, um filtro Where
    # (Seguindo o exemplo do select) para saber qual registro editar,
    # e os novos valores
    def edit(self, tabela, where, valores):
        # Pega o nome do arquivo.
        filename = self.getJSON(self, tabela)
        # Abre o arquivo
        with open(filename) as file:
            # Carrega o arquivo em uma variável
            banco = json.load(file)
            # Pega o tamanho do arquivo para usar em um laço.
            length = len(banco[tabela])
            # Para cada item existente
            for row in range(length):
                # Verifica se o campo bate com o valor do where
                if banco[tabela][row][where[0]] == str(where[1]):
                    # Seta os novos dados recebidos
                    banco[tabela][row] = valores
            # Abre o arquivo com permissão de escrita
            with open(filename, 'w') as file:
                # Salva o novo arquivo atualizado
                json.dump(banco, file, indent=4)
        # Retorno
        return True