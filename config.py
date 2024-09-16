import os

class Config:
    # URL de conexão com o banco de dados PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://flask_user:flasksenha@localhost:5432/flask_db')
    # Desativa a rastreamento de modificações para economizar recursos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Chave secreta para sessões e segurança
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')

