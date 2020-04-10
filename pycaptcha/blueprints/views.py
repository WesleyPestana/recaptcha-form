import requests
from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, login_user, logout_user
from sqlalchemy.exc import IntegrityError
from pycaptcha.ext.auth import login_manager
from pycaptcha.ext.database import db
from pycaptcha.models import Usuario

usuarios_bp = Blueprint('usuarios', __name__)


def init_app(app):
    app.register_blueprint(usuarios_bp)


@usuarios_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@usuarios_bp.route('/cadastrar/', methods=['GET', 'POST'])
def cadastrar():
    errors = {}

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirma_senha = request.form['c_senha']
        recaptcha_response = request.form['g-recaptcha-response']

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LetuOYUAAAAAOH0J2P-xYVT_jJXM7NPTuj9jRyP',
                'response': recaptcha_response
            }
        ).json()
        print(recaptcha_request)

        if senha != confirma_senha:
            errors['senha'] = True
        if not recaptcha_request.get('success'):
            errors['recaptcha'] = True

        if errors:
            return render_template('cadastrar.html', errors=errors, nome=nome, email=email)

        try:
            usuario = Usuario(nome, email, senha)
            db.session.add(usuario)
            db.session.commit()
        except IntegrityError:
            errors['email'] = True
            return render_template('cadastrar.html', errors=errors, nome=nome, email=email)


        return redirect('/login/')

    return render_template('cadastrar.html', errors=errors)


@usuarios_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario.query.filter_by(email=email).first()

        if not usuario or not usuario.verificar_senha(senha):
            return redirect('/login/')

        login_user(usuario)
        return redirect('/perfil/')

    return render_template('login.html')


@usuarios_bp.route('/logout/')
def logout():
    logout_user()
    return redirect('/login/')


@usuarios_bp.route('/perfil/', methods=['GET'])
@login_required
def perfil():
    return render_template('perfil.html', autenticado=True)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login/')
