
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def industriaswayne():
    return render_template("index.html")
#industriaswayne.com/

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

if __name__=="__main__":
    app.run(debug=True)