from database import db
from sqlalchemy import Integer, String
from werkzeug.security import generate_password_hash, check_password_hash


class Login(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    email = db.Column('email', db.String, nullable=False)
    senha = db.Column('senha', db.String, nullable=False)
    
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

class Register(db.Model):
    __tablename__ = 'register'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column('nome', db.String, nullable=False)
    sobrenome = db.Column('sobrenome', db.String, nullable=False)
    email = db.Column('email', db.String, nullable=False, unique=True)
    telefone = db.Column('telefone', db.String)
    senha = db.Column('senha', db.String, nullable=False)
    confirm_senha = db.Column('confirm_senha', db.String, nullable=False)

    def __init__(self, nome, sobrenome, email, telefone, senha, confirm_senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone
        self.senha = generate_password_hash(senha)
        self.confirm_senha = confirm_senha

    def verify_password(self, senha):
        return check_password_hash(self.senha)