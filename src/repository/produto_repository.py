from src.database.conexao import BancoDeDados
from src.models.produto_model import ProdutoModel


class ProdutoRepository:
    def criar(self, produto: ProdutoModel):
        sql = """
            INSERT INTO produtos (nome, descricao, preco)
            VALUES (%s, %s, %s)
            RETURNING id;
        """
        with BancoDeDados() as cursor:
            cursor.execute(sql, (produto.nome, produto.descricao, produto.preco))
            return cursor.fetchone()[0]

    def listar_todos_com_estoque(self):
        sql = """
            SELECT p.id, p.nome, p.descricao, p.preco, e.quantidade
            FROM produtos p
            JOIN estoque e ON p.id = e.produto_id
            ORDER BY p.id DESC;
        """
        resultados = []
        with BancoDeDados() as cursor:
            cursor.execute(sql)
            for row in cursor.fetchall():
                resultados.append({
                    "id": row[0],
                    "nome": row[1],
                    "descricao": row[2],
                    "preco": row[3],
                    "quantidade": row[4]
                })
        return resultados

    def buscar_por_id(self, produto_id):
        sql = """
            SELECT id, nome, descricao, preco FROM produtos WHERE id = %s;
        """
        with BancoDeDados() as cursor:
            cursor.execute(sql, (produto_id,))
            row = cursor.fetchone()
            if row:
                return {"id": row[0], "nome": row[1], "descricao": row[2], "preco": row[3]}
            return None

    def atualizar(self, produto_id, nome, descricao, preco):
        sql = """
            UPDATE produtos SET nome = %s, descricao = %s, preco = %s WHERE id = %s;
        """
        with BancoDeDados() as cursor:
            cursor.execute(sql, (nome, descricao, preco, produto_id))