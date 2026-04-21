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