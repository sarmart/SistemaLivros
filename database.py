from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):

    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:1234@localhost:3306/novo'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

with db.app_context():
    db.drop_all()
    db.create_all()
    print("Database.py funcionando."), current_app