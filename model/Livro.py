from database import db

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=True)
    isbn = db.Column(db.String(20), unique=True, nullable=True)
    data_publicacao = db.Column(db.Date, nullable=True)
    numero_paginas = db.Column(db.Integer, nullable=True)
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=True)
    
    autor = db.relationship('Autor', back_populates='livros')
    categoria = db.relationship('Categoria', back_populates='livros')

    def toJson(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "isbn": self.isbn,
            "data_publicacao": self.data_publicacao,
            "numero_paginas": self.numero_paginas,
            "autor": self.autor.toJson() if self.autor else None,
            "categoria": self.categoria
        }