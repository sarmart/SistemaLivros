from model import Livro, db

class LivroDao:
    @staticmethod
    # app.route('/livros', methods['GET'])
    
    def all_livros(): # Consultar todos os livros
        return Livro.query.all()

    @staticmethod
    def src_livros_titulo(titulo): # Pesquisar por titulo
        pass

    @staticmethod
    def src_livros_isbn(isbn): # Pesquisa por isbn
        pass

    @staticmethod
    def criar(livro):
        pass