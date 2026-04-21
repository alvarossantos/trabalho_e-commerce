# 🛒 E-Commerce Lite (Sistema de Catálogo)

Um sistema web simples de catálogo de produtos com controle de estoque, desenvolvido em Python com Flask e PostgreSQL. Este projeto foi construído aplicando rigorosamente os conceitos de **Arquitetura Lógica em Três Camadas**, separando responsabilidades de apresentação, regras de negócio e acesso a dados.

## ✨ Funcionalidades

* **Listagem de Produtos:** Visualização de todos os produtos cadastrados e seus respectivos estoques.
* **Cadastro:** Adição de novos produtos com definição de estoque inicial.
* **Edição (Update):** Modificação dos dados básicos de produtos existentes.
* **Controle de Estoque (Entrada/Saída):**
    * **Venda (Saída):** Simulação de compra com baixa automática e validada no estoque. Impede vendas com saldo negativo.
    * **Reposição (Entrada):** Adição de unidades ao estoque de um produto existente.

## 🏗️ Arquitetura do Sistema

### 1. Arquitetura Lógica (Três Camadas)
O código fonte está organizado de forma a garantir a separação de responsabilidades:

* **Camada de Apresentação (Views/Rotas):**
    * Composta pelo framework Flask (`app.py`) e pelos templates HTML (`src/views/templates/`).
    * *Responsabilidade:* Receber as interações do usuário pelo navegador, repassar as solicitações para os Controladores e renderizar o HTML final de volta para o cliente.
* **Camada de Lógica de Negócio (Controllers/Models):**
    * Localizada nas pastas `src/controllers/` e `src/models/`.
    * *Responsabilidade:* Orquestrar as ações. Valida regras de negócio (ex: preço não pode ser negativo, venda não pode ocorrer sem estoque) antes de permitir qualquer alteração no banco de dados. Os *Models* representam as entidades do sistema em memória.
* **Camada de Acesso a Dados (Repositories):**
    * Localizada na pasta `src/repository/` e `src/database/`.
    * *Responsabilidade:* Isolar toda a comunicação e execução de código SQL (comandos `INSERT`, `UPDATE`, `SELECT`). As outras camadas do sistema não escrevem SQL diretamente.

### 2. Arquitetura Física de Implantação
Para implantar este sistema num cenário real, a arquitetura física seguiria o modelo **Cliente-Servidor**:

* **Cliente (Client-Side):**
    * Qualquer dispositivo (PC, Mobile) rodando um Navegador Web (Chrome, Firefox). O navegador é responsável apenas por renderizar as telas HTML e enviar as requisições.
* **Servidor de Aplicação (Backend):**
    * Uma máquina virtual em nuvem (ex: AWS EC2, DigitalOcean Droplet, Render) responsável por executar o código Python/Flask, processando a lógica de negócio de forma centralizada.
* **Servidor de Banco de Dados:**
    * Um serviço hospedando o PostgreSQL. Pode estar instalado na mesma máquina do servidor de aplicação (para economizar recursos em ambientes menores) ou em um servidor/serviço gerenciado exclusivo (ex: AWS RDS).
* **Comunicação:** O cliente e o servidor de aplicação se comunicam pela internet via protocolo **HTTP/HTTPS**. O servidor de aplicação e o banco de dados se comunicam via protocolo **TCP/IP**.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3, Flask
* **Banco de Dados:** PostgreSQL (driver `psycopg2-binary`)
* **Frontend:** HTML5, CSS3, Bootstrap 5 (via CDN para interface)
* **Gerenciamento de Variáveis:** `python-dotenv`

## 📂 Estrutura de Pastas

```text
projeto-ecommerce-lite/
├── app.py                   # Ponto de entrada (Rotas Web / Apresentação)
├── banco.sql                # Script de criação das tabelas do banco
├── requirements.txt         # Dependências do projeto (Flask, psycopg2)
├── .env.example             # Modelo para variáveis de ambiente
└── src/
    ├── controllers/         # Regras de Negócio
    │   └── produto_controller.py
    ├── models/              # Estrutura dos Dados
    │   ├── produto_model.py
    │   └── estoque_model.py
    ├── repository/          # Execução de SQL e persistência
    │   ├── produto_repository.py
    │   └── estoque_repository.py
    ├── database/            # Conexão centralizada com o banco
    │   └── conexao.py
    └── views/
        └── templates/       # Telas HTML (Interface)
            ├── base.html
            ├── index.html
            ├── cadastro.html
            └── editar.html
```

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
* Python 3.x instalado.
* PostgreSQL instalado e rodando.

### Passos de Instalação

1. **Clone o repositório ou extraia os arquivos:**
   Abra o terminal na pasta do projeto.

2. **Crie e ative o ambiente virtual (Recomendado):**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o Banco de Dados:**
   * Crie um banco de dados no seu PostgreSQL (ex: `e-commerce`).
   * Rode o script `banco.sql` na sua ferramenta de banco (PgAdmin, DBeaver, ou psql) para criar as tabelas `produtos` e `estoque`.
   * Crie um arquivo chamado `.env` na raiz do projeto (ao lado do `app.py`) contendo as suas credenciais:
     ```env
     DB_NAME=e-commerce
     DB_USER=postgres
     DB_PASSWORD=sua_senha
     DB_HOST=localhost
     DB_PORT=5432
     ```

5. **Inicie a aplicação:**
   ```bash
   python app.py
   ```

6. **Acesse:** Abra o navegador e acesse `http://127.0.0.1:5000/`.

## 🗄️ Esquema do Banco de Dados

O projeto utiliza um modelo simples e relacional focado na gestão do catálogo:

* **Tabela `produtos`:** Armazena os dados primários (`id`, `nome`, `descricao`, `preco`).
* **Tabela `estoque`:** Armazena a `quantidade` atual, relacionada com a tabela `produtos` via chave estrangeira (`produto_id`). Utiliza a regra `ON DELETE CASCADE` para manter a integridade (se um produto sumir, seu estoque some junto).