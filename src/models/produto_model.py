# ==========================================
# CAMADA DE DADOS (Models)
# ==========================================
# Este arquivo apenas define a estrutura do objeto.
# Serve para padronizar os dados que circulam entre as camadas.
class ProdutoModel:
    def __init__(self, nome, descricao, preco, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco