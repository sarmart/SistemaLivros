from dao import LivroDao

class LivroRepos:
    def __init__(self) -> None:
        self.livroDao = LivroDao()

    def all_livros(self):
        return self.livroDao.all_livros()
    
    def criar(self, titulo, isbn, data_publicacao, numero_paginas): #autor
        return self.livroDao.criar(titulo, isbn, data_publicacao, numero_paginas) #autor