from database import db

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    
    livros = db.relationship('Livro', back_populates='categoria')