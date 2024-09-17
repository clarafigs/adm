import os

class Config:

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://flask_user:flasksenha@localhost:5432/flask_db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')

