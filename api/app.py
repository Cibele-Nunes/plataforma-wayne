
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def industriaswayne():
    return render_template("homepage.html")
#industriaswayne.com/
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

if __name__=="__main__":
    app.run(debug=True)