
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from database import db
from modelos import Login, Register


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db.init_app(app)

@app.route("/")
def industriaswayne():
    return render_template("index.html")
#industriaswayne.com/

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        telefone = request.form['telefone']
        senha = request.form['senha']
        confirm_senha = request.form['confirm_senha']

        usuario = Register(nome, sobrenome, email, telefone, senha, confirm_senha)
        db.session.add(usuario)
        db.session.commit()
    
    return render_template('register.html', nome='nome', sobrenome='sobrenome', email='email', telefone='telefone', senha='senha', confirm_senha='confirm_senha')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)