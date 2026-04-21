import os
from flask import Flask, render_template, request, redirect, flash
from src.controllers.produto_controller import ProdutoController


caminho_templates = os.path.abspath('src/views/templates')
app = Flask(__name__, template_folder=caminho_templates)
app.secret_key = 'chave_secreta'

controller = ProdutoController()

@app.route('/')
def index():
    produtos = controller.listar_produtos()
    return render_template('index.html', produtos=produtos)

@app.route('cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        quantidade = request.form.get('quantidade')

        sucesso, mensagem = controller.cadastrar_produto_com_estoque(nome, descricao, preco, quantidade)

        if sucesso:
            flash(mensagem, 'success')
            return redirect('/')
        else:
            flash(mensagem, 'danger')

    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)