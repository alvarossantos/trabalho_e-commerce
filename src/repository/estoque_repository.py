from src.database.conexao import BancoDeDados


class EstoqueRepository:
    def criar_estoque_inicial(self, produto_id, quantidade):
        sql = """
            INSERT INTO estoque (produto_id, quantidade) VALUES (%s, %s);
        """
        with BancoDeDados() as cursor:
            cursor.execute(sql, (produto_id, quantidade))