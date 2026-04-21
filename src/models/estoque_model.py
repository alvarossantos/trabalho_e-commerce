# ==========================================
# CAMADA DE DADOS (Models)
# ==========================================
# Este arquivo apenas define a estrutura do objeto.
# Serve para padronizar os dados que circulam entre as camadas.
class EstoqueModel:
    def __init__(self, produto_id, quantidade):
        self.produto_id = produto_id
        self.quantidade = quantidade