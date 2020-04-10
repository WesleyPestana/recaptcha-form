from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from pycaptcha.ext.database import db
from pycaptcha.ext.auth import login_manager


@login_manager.user_loader
def buscar_usuario(id_usuario):
    return Usuario.query.filter_by(id=id_usuario).first()


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(80), nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha, senha)
