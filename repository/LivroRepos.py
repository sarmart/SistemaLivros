from dao import LivroDao

class LivroRepos:
    def __init__(self) -> None:
        self.livroDao = LivroDao()

    def all_livros(self):
        return self.livroDao.all_livros()