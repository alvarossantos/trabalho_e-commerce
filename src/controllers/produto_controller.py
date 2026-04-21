from src.models.produto_model import ProdutoModel
from src.repository.estoque_repository import EstoqueRepository
from src.repository.produto_repository import ProdutoRepository


class ProdutoController:
    def __init__(self):
        self.produto_repo = ProdutoRepository()
        self.estoque_repo = EstoqueRepository()

    def cadastrar_produto_com_estoque(self, nome, descricao, preco, quantidade_inicial):
        if float(preco) <= 0:
            return False, "O preço deve ser maior que zero."
        if int(quantidade_inicial) < 0:
            return False, "A quantidade em estoque não pode ser negativa."

        produto = ProdutoModel(nome, descricao, float(preco))

        try:
            novo_produto_id = self.produto_repo.criar(produto)
            self.estoque_repo.criar_estoque_inicial(novo_produto_id, int(quantidade_inicial))

            return True, "Produto e estoque cadastrados com sucesso!"

        except Exception as e:
            print(f"Erro no banco: {e}")
            return False, "Erro interno ao salvar no banco de dados."

    def listar_produtos(self):
        return self.produto_repo.listar_todos_com_estoque()

    def buscar_produto_para_edicao(self, produto_id):
        return self.produto_repo.buscar_por_id(produto_id)

    def atualizar_dados_produto(self, produto_id, nome, descricao, preco):
        if float(preco) <= 0:
            return False, "O preço deve ser maior que zero."

        try:
            self.produto_repo.atualizar(produto_id, nome, descricao, float(preco))
            return True, "Produto atualizado com sucesso!"
        except Exception as e:
            print(f"Erro no banco: {e}")
            return False, "Erro ao atualizar produto."

    def realizar_venda(self, produto_id, quantidade):
        if int(quantidade) <= 0:
            return False, "A quantidade comprada deve ser maior que zero."

        sucesso = self.estoque_repo.baixar_estoque(produto_id, int(quantidade))

        if sucesso:
            return True, f"Compra de {quantidade} unidade(s) realiza com sucesso! Obrigado."
        else:
            return False, "Desculpe, estoque insuficiente para essa quantidade."

    def repor_estoque(self, produto_id, quantidade):
        if int(quantidade) <= 0:
            return False, "A quantidade de reposição deve ser maior que zero."

        try:
            sucesso = self.estoque_repo.adicionar_estoque(produto_id, int(quantidade))
            if sucesso:
                return True, "Estoque atualizado com sucesso!"
            else:
                return False, "Erro: Produto não encontrado no estoque."
        except Exception as e:
            print(f"Erro no banco ao repor estoque: {e}")
            return False, "Erro interno ao atualizar o estoque."