from database import db

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nacionalidade = db.Column(db.String(50), nullable=False)
    
    livros = db.relationship('Livro', back_populates='autor')