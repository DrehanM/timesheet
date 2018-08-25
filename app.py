from flask import Flask, render_template, request, jsonify
import sqlite3
import hashlib

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>timesheet</h1><p>keeping track of your time for you.</p>"

@app.route('/register', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']

    hashcode = get_hash(password)

    add_user(username, password)

def add_user(username : str, hashcode : int) -> None:
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    user_exists = cur.execute('SELECT username FROM USERS WHERE username=?', [username]).fetchall()
    if user_exists:
        conn.close()
        return 'The username, {}, is taken.'.format(username)
    cur.execute('INSERT INTO USERS (username, hashcode) VALUES (?, ?)', (username, hashcode))
    conn.commit()
    conn.close()

@app.route('/login', methods=['GET'])
def login():
    username = request.form['username']
    password = request.form['password']

    hashcode = get_hash(password)

    verified = verify_user(username, hashcode)

def verify_user(username : str, hashcode : int) -> bool:
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    user_info = cur.execute('SELECT * FROM USERS WHERE username=? AND hashcode=?', [username, hashcode]).fetchall()
    if username == user_info[0] and hashcode == user_info[1]:
        return True
    return False



@app.errorhandler(404)
def page_not_found():
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

def get_hash(object):
    return int(hashlib.sha1(object).hexdigest(), 16) % (10 ** 8)
    


app.run()