class ProdutoModel:
    def __init__(self, nome, descricao, preco, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco