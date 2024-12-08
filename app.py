from flask import Flask, jsonify, request  # type: ignore
from database import init_db, db
from repository import LivroRepos

app = Flask(__name__)

livroRepos = LivroRepos()

@app.route('/')
def index():
    return 'Hello! Bem-vindo.'

@app.route('/livros', methods=['GET'])
def livros():
    livros = livroRepos.all_livros()
    print(livros)
    return jsonify([livro.toJson() for livro in livros])

@app.route('/livros/criar', methods=['POST'])
def criar():
    titulo = request.json.get('titulo')
    isbn = request.json.get('isbn')
    data_publicacao = request.json.get('data_publicacao')
    numero_paginas = request.json.get('numero_paginas')
    # autor = request.json.get('autor')
    livros = livroRepos.criar(titulo, isbn, data_publicacao, numero_paginas)
    print(livros)
    return jsonify(livros.toJson())

@app.route('/livros/excluir/<int:livro_id>', methods=['DELETE'])
def excluir(livro_id):
    livro_exc = livroRepos.excluir(livro_id)
    if livro_exc:
        return jsonify({'message': 'Excluido com sucesso'}), 200
    return jsonify({'message':'Não encontrado.'}), 404


if __name__ == "__main__":
    init_db(app)
    app.run(debug = True)




# Operações - marcar quando funcionar corretamente: 
# [] cadastrar ; [] excluir ; [] editar ; [x]consultar todos ; 
# [] consulta específica (título, autor, categoria ou ISBN) ; [x] exibir. <- Tudo em DAO?
# Adicionar...
# [] Blueprint ; [] JSON ; [] Sessions

# "Etapas" para serem cumpridas sem minha cabeça explodir:
# (I) Configuracao básica [x]
# (II) Tabelas [x]
# (III) DAO/Repositório []
# (IV) Rotas []
# (V) Teste [] 
# (VI) View []

# app.route('/livros', methods['GET'])