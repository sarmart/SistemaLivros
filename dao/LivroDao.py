from model import Livro, Autor, db
from datetime import datetime

class LivroDao:
    @staticmethod
    # app.route('/livros', methods['GET'])

    def all_livros(): # Consultar todos os livros
        l = Livro.query.all()
        return l

    @staticmethod
    def criar(titulo, isbn, data_publicacao, numero_paginas, autor):
        data_publicacao_date = datetime.strptime(data_publicacao, "%Y-%m-%d").date()
        # add all e commit
        
        #tentar diminuir aqui transformando em func em Autor.
        autor =  Autor.query.filter(Autor.nome == autor).first() #verifica se existe...
        if autor is None:
            autor = Autor(nome = autor)
            db.session.add(autor)
            db.session.commit()

        livro = Livro(titulo=titulo, isbn=isbn, data_publicacao=data_publicacao_date, numero_paginas=numero_paginas, autor=autor)
        db.session.add(livro)
        db.session.commit()
        return livro
    
    @staticmethod
    def excluir(id):
        livro = Livro.query.get(id)
        if livro:
            db.session.delete(livro)
            db.session.commit()
        return livro

    @staticmethod
    def src_livros_titulo(titulo): # Pesquisar por titulo
        pass

    @staticmethod
    def src_livros_isbn(isbn): # Pesquisa por isbn
        pass