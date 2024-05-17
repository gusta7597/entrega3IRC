from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'db',
    'user': 'root',
    'password': '123',
    'database': 'soprojeto'
}

@app.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM usuario')
    usuarios = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', usuarios=usuarios)

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    email = request.form['email']
    cpf = request.form['cpf']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('INSERT INTO usuario (nome, email, cpf) VALUES (%s, %s, %s)', (nome, email, cpf))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM usuario WHERE id = %s', (id,))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('index'))
