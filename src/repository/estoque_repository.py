# ==========================================
# CAMADA DE ACESSO AO BANCO (Repository)
# ==========================================
# Este arquivo é o ÚNICO lugar onde escrevemos comandos SQL.
# Ele se comunica direto com o banco de dados.
from src.database.conexao import BancoDeDados


class EstoqueRepository:
    def criar_estoque_inicial(self, produto_id, quantidade):
        # Comando SQL para inserir um novo registro
        sql = """
            INSERT INTO estoque (produto_id, quantidade) VALUES (%s, %s);
        """
        with BancoDeDados() as cursor:
            cursor.execute(sql, (produto_id, quantidade))

    def baixar_estoque(self, produto_id, quantidade_comprada=1):
        # Diminui a quantidade no estoque, garantindo que não fique negativo
        sql = """
            UPDATE estoque
            SET quantidade = quantidade - %s
            WHERE produto_id = %s AND quantidade >= %s;
        """
        with BancoDeDados() as cursor:
            cursor.execute(sql, (quantidade_comprada, produto_id, quantidade_comprada))
            return cursor.rowcount > 0

    def adicionar_estoque(self, produto_id, quantidade_adicional):
        # Aumenta a quantidade do estoque
        sql = """
            UPDATE estoque
            SET quantidade = quantidade + %s
            WHERE produto_id = %s;
        """
        with BancoDeDados() as cursor:
            cursor.execute(sql, (quantidade_adicional, produto_id))
            return cursor.rowcount > 0