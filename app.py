from flask import Flask , render_template

app = Flask(__nome__)
app.route('/')
def hello_world():
    return render_template("inicio.html")

app.route('/formulário_do_aluno')
def formulário_do_aluno():
    return render_template("formulário_do_aluno.html") 