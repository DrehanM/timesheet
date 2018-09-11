from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
from functools import wraps
from hashlib import sha1
from models import get_user, create_post, get_posts

app = Flask(__name__)

CORS(app)

def authorize(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        request_id = sha1()

        if auth:
            request_id.update(bytes(auth.username, encoding="utf-8"))
            request_id.update(bytes(auth.password, encoding="utf-8"))
            hash_id = int(float('%f' % (int(request_id.hexdigest(), 16) % 1e18)))

            returned_user = get_user(hash_id)
            if returned_user:
                return f(returned_user)
                
        return make_response('Could not verify.', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
    return decorated
 
@app.route('/', methods=['GET', 'POST'])
@authorize
def index(username):
    return'<h1>Hello World</h1>'

@app.route('/login')
@authorize
def login(username):
    return render_template('index.html', posts='')

@app.route('/register')
def register():
    return '<h1> Register here</h1>'

@app.route('/user/<string:username>')
@authorize
def profile(username):
    username = username[0][0]
    return render_template('profile.html', username=username)



if __name__ == '__main__':
    app.run(debug=True)