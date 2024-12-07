from flask import Flask, jsonify, Response, request  # type: ignore
from database import init_db, db
from repository import LivroRepos

app = Flask(__name__)

livroRepos = LivroRepos()

@app.route('/')
def index():
    return 'Hello!'

@app.route('/livros', methods=['GET'])
def livros():
    livros = livroRepos.all_livros()
    print(livros)
    return jsonify([livro.toJson() for livro in livros]), Response()

if __name__ == "__main__":
    init_db(app)
    app.run(debug = True)





# Operações - marcar quando funcionar corretamente: 
# [] cadastrar ; [] excluir ; [] editar ; []consultar ; [] exibir. <- Tudo em DAO?
# Adicionar...
# [] Blueprint ; [] JSON ; [] Sessions

# "Etapas" para serem cumpridas sem minha cabeça explodir:
# (I) Configuracao básica [x]
# (II) Tabelas [x]
# (III) DAO/Repositório []
# (IV) Rotas []
# (V) Teste [] <- tentar mexer no postman dnv
# (VI) View []

# app.route('/livros', methods['GET'])