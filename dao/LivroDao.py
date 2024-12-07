from model import Livro, db

class LivroDao:
    @staticmethod
    # app.route('/livros', methods['GET'])

    def all_livros(): # Consultar todos os livros
        l = Livro.query.all()
        return l

    @staticmethod
    def src_livros_titulo(titulo): # Pesquisar por titulo
        pass

    @staticmethod
    def src_livros_isbn(isbn): # Pesquisa por isbn
        pass

    @staticmethod
    def criar(titulo):
        # add all e commit
        livro = Livro(titulo=titulo)
        db.session.add(livro)
        db.session.commit()
        return livro