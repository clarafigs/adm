
from extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    loginUser = db.Column(db.String(50), primary_key=True)
    senha = db.Column(db.String(200), nullable=False)
    tipoUser = db.Column(db.String(10), nullable=False)

class Produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    loginUser = db.Column(db.String(50), db.ForeignKey('usuarios.loginUser'), nullable=False)
    qtde = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)


