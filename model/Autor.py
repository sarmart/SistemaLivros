from database import db

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=True)
    data_nascimento = db.Column(db.Date, nullable=True)
    nacionalidade = db.Column(db.String(50), nullable=True)
    
    livros = db.relationship('Livro', back_populates='autor')

    def toJson(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "nacionalidade": self.nacionalidade
        }