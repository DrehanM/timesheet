from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts
import hashlib, binascii

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        pass
    
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    posts = get_posts()


    return render_template('index.html', posts=posts)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    
    


if __name__ == '__main__':
    app.run(debug=True)