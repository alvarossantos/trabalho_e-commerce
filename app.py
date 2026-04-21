import os
from pydoc import describe

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

@app.route('/cadastrar', methods=['GET', 'POST'])
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

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')

        sucesso, mensagem = controller.atualizar_dados_produto(id, nome, descricao, preco)

        if sucesso:
            flash(mensagem, 'success')
            return redirect('/')
        else:
            flash(mensagem, 'danger')

    produto = controller.buscar_produto_para_edicao(id)
    if not produto:
        flash('Produto não encontrado', 'warning')
        return redirect('/')

    return render_template('editar.html', produto=produto)

@app.route('/comprar/<int:id>', methods=['POST'])
def comprar(id):
    quantidade = request.form.get('quantidade')

    sucesso, mensagem = controller.realizar_venda(id, quantidade)

    if sucesso:
        flash(mensagem, 'success')
    else:
        flash(mensagem, 'warning')

    return redirect('/')

@app.route('/repor/<int:id>', methods=['POST'])
def repor(id):
    quantidade = request.form.get('quantidade')

    sucesso, mensagem = controller.repor_estoque(id, quantidade)

    if sucesso:
        flash(mensagem, 'success')
    else:
        flash(mensagem, 'warning')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)