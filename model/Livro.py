from database import db

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    data_publicacao = db.Column(db.Date, nullable=False)
    numero_paginas = db.Column(db.Integer, nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    
    autor = db.relationship('Autor', back_populates='livros')
    categoria = db.relationship('Categoria', back_populates='livros')