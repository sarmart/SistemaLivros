from dao import LivroDao

class LivroRepos:
    def __init__(self) -> None:
        self.livroDao = LivroDao()

    def all_livros(self):
        return self.livroDao.all_livros()
    
    def criar(self, titulo, isbn, data_publicacao, numero_paginas, autor): #autor
        return self.livroDao.criar(titulo, isbn, data_publicacao, numero_paginas, autor) #autor
    
    def excluir(self, livro_id):
        return self.livroDao.excluir(livro_id)
