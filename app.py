import os
from flask import Flask, render_template, request, redirect, flash
from src.controllers.produto_controller import ProdutoController

# ==========================================
# CAMADA DE APRESENTAÇÃO (Rotas e Telas)
# ==========================================
# Este arquivo gerencia as rotas web (URLs).
# Ele recebe os dados do usuário, chama o Controller para processar
# e devolve a tela HTML pronta. Aqui não vai SQL nem regras de negócio.

caminho_templates = os.path.abspath('src/views/templates')
app = Flask(__name__, template_folder=caminho_templates)
app.secret_key = 'chave_secreta'

controller = ProdutoController()

@app.route('/')
def index():
    # Pega a lista de produtos do controller para mostrar na tela principal
    produtos = controller.listar_produtos()
    return render_template('index.html', produtos=produtos)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        quantidade = request.form.get('quantidade')

        # Envia os dados do formulário para o controller processar o cadastro
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

        # Envia os novos dados para o controller salvar a edição
        sucesso, mensagem = controller.atualizar_dados_produto(id, nome, descricao, preco)

        if sucesso:
            flash(mensagem, 'success')
            return redirect('/')
        else:
            flash(mensagem, 'danger')

    # Carrega os dados do produto para preencher os campos na tela de edição
    produto = controller.buscar_produto_para_edicao(id)
    if not produto:
        flash('Produto não encontrado', 'warning')
        return redirect('/')

    return render_template('editar.html', produto=produto)

@app.route('/comprar/<int:id>', methods=['POST'])
def comprar(id):
    quantidade = request.form.get('quantidade')

    # Tenta realizar a venda através do controller
    sucesso, mensagem = controller.realizar_venda(id, quantidade)

    if sucesso:
        flash(mensagem, 'success')
    else:
        flash(mensagem, 'danger')

    return redirect('/')

@app.route('/repor/<int:id>', methods=['POST'])
def repor(id):
    quantidade = request.form.get('quantidade')

    # Tenta repor o estoque através do controller
    sucesso, mensagem = controller.repor_estoque(id, quantidade)

    if sucesso:
        flash(mensagem, 'success')
    else:
        flash(mensagem, 'danger')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)