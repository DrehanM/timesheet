from flask import Flask, render_template, request, jsonify
import sqlite3
import hashlib
import os

app = Flask(__name__, template_folder= os.path.join(os.getcwd(), 'templates/'))
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register_user():
    username = request.form.get('username', None)
    password = request.form.get('password', None)

    hashcode = get_hash(password)

    ok = add_user(username, hashcode)

    return render_template('index.html') if ok else page_not_found()

def add_user(username : str, hashcode : int) -> bool:
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    user_exists = cur.execute('SELECT username FROM USERS WHERE username=?', [username]).fetchall()
    print(user_exists)
    if user_exists:
        conn.close()
        print('The username, {}, is taken.'.format(username))
        return False
    cur.execute('INSERT INTO USERS (username, hashcode) VALUES (?, ?)', (username, hashcode))
    conn.commit()
    conn.close()
    return True

@app.route('/login', methods=['GET'])
def login():
    username = request.form.get('username', str)
    password = request.form.get('password', str)

    print(password)

    hashcode = get_hash(password)

    verified = verify_user(username, hashcode)

    if verified:
        print("Welcome")
    else:
        print("Wrong credentials")

def verify_user(username : str, hashcode : int) -> bool:
    print((username, hashcode))
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    user_info = cur.execute('SELECT * FROM USERS WHERE username=? AND hashcode=?', [username, hashcode]).fetchall()
    conn.close()
    if username == user_info[0] and hashcode == user_info[1]:
        return True
    return False

@app.errorhandler(404)
def page_not_found():
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

def get_hash(object):
    return int(hashlib.sha1(object.encode('utf-8')).hexdigest(), 16) % (10 ** 8)
    


app.run()