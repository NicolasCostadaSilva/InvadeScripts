from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

def database_exists(filename):
    return os.path.isfile(filename)

# Função para criar o banco de dados e a tabela de usuários
def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT
                    )''')
    conn.commit()
    conn.close()

# Função para adicionar um novo usuário ao banco de dados
def add_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    conn.commit()
    conn.close()

# Função para verificar se as credenciais do usuário estão corretas
def verify_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
    user = cursor.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False

# Verifica se já temos o usuário cadastrado
def verify_username(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if verify_user(username, password):
            return "Login bem-sucedido!"
        else:
            return "Credenciais inválidas."
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if verify_username(username):
            return "Usuário já existe. Escolha outro nome de usuário."
        else:
            add_user(username, password)
            return "Usuário registrado com sucesso!"
    else:
        return render_template('register.html')

if __name__ == '__main__':
    if not database_exists('users.db'):
        create_database()
    app.run(debug=True, port=1234)
