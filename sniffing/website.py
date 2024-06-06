from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' #para o funcionamento do banco de dados
db = SQLAlchemy(app) #para o funcionamento do banco de dados

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True) #Seto o Id do Usuario
    username = db.Column(db.String(80), unique = True, nullable = False) #Nome do usuario
    password = db.Column(db.String(120), nullable = False) #Senha do usuario

@app.route('/')
def home(): #pagina de entrada
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register(): #registramos o usuario e adicionamos no banco de dados
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username = username, password = password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods = ['GET', 'POST'])
def login(): #verificamos se o usuario existe ou nao foi inserido nada errado, e o logamos caso tudo esteja certo
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username = username, password = password).first()
        if user:
            return "logado com sucesso", 200
        else:
            error = "Nome de usuário ou senha inválidos"
            return render_template('login.html', error=error), 401
    return render_template('login.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=1234) #iniciamos o servidor flask - mudar a porta para o que voce deseja