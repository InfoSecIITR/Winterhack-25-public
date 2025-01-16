import flask
from flask import render_template
import sqlite3
import os

app = flask.Flask(__name__)
FLAG = os.environ.get('FLAG', 'winterhack{this_is_a_fake_flag}')

def init_db():
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    admin_password = os.environ.get('ADMIN_PASSWORD', 'admin')
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT, password TEXT)')
    c.execute('INSERT INTO users (username, password) VALUES ("admin", ?)', (admin_password,))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = flask.request.form['username']
    password = flask.request.form['password']
    
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = "{}" and password = "{}"'.format(username, password))
    result = c.fetchone()
    conn.close()

    if result is None:
        return render_template('response.html', message='Username or password is incorrect!')
    return render_template('response.html', message=f"Welcome {FLAG}!")

if __name__ == '__main__':
    if not os.path.exists('login.db'):
        init_db()
    app.run(host="0.0.0.0")
