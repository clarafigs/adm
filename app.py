import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from extensions import db
from models import Usuario, Produto
from werkzeug.security import generate_password_hash, check_password_hash

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://flask_user:flasksenha@localhost:5432/flask_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar o banco de dados
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if 'loginUser' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    loginUser = request.form['loginUser']
    senha = request.form['senha']
    user = Usuario.query.filter_by(loginUser=loginUser).first()

    if user and check_password_hash(user.senha, senha):
        session['loginUser'] = user.loginUser
        session['tipoUser'] = user.tipoUser
        return redirect(url_for('dashboard'))

    flash('Login ou senha incorretos')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'loginUser' not in session:
        return redirect(url_for('index'))
    produtos = Produto.query.filter_by(loginUser=session['loginUser']).all()
    return render_template('dashboard.html', produtos=produtos)

@app.route('/cadastrar_usuario', methods=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        loginUser = request.form['loginUser']
        senha = request.form['senha']
        tipoUser = request.form['tipoUser']
        hashed_password = generate_password_hash(senha, method='sha256')

        novo_usuario = Usuario(loginUser=loginUser, senha=hashed_password, tipoUser=tipoUser)
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Usuário cadastrado com sucesso!')
        return redirect(url_for('index'))

    return render_template('cadastrar_usuario.html')

@app.route('/cadastrar_produto', methods=['GET', 'POST'])
def cadastrar_produto():
    if 'loginUser' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        nome = request.form['nome']
        qtde = request.form['qtde']
        preco = request.form['preco']

        if session['tipoUser'] == 'normal':
            produtos_count = Produto.query.filter_by(loginUser=session['loginUser']).count()
            if produtos_count >= 3:
                flash('Usuário normal pode cadastrar no máximo 3 produtos.')
                return redirect(url_for('dashboard'))

        novo_produto = Produto(nome=nome, qtde=qtde, preco=preco, loginUser=session['loginUser'])
        db.session.add(novo_produto)
        db.session.commit()

        flash('Produto cadastrado com sucesso!')
        return redirect(url_for('dashboard'))

    return render_template('cadastrar_produto.html')

@app.route('/logout')
def logout():
    session.pop('loginUser', None)
    session.pop('tipoUser', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

