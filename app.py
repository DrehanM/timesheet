from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
from functools import wraps
from hashlib import sha1
from models import get_user, register_user
from utils import hash_it, hash_login, hash256_it, hash256_login

app = Flask(__name__)

CORS(app)

def authorize(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        #request_id = sha1()

        if auth:
            '''
            request_id.update(bytes(auth.username, encoding="utf-8"))
            request_id.update(bytes(auth.password, encoding="utf-8"))
            user_id = int(float('%f' % (int(request_id.hexdigest(), 16) % 1e18)))
            '''

            user_id = hash256_login(auth.username, auth.password)
            returned_user = get_user(user_id)

            if returned_user:
                user_info = {
                    'user_id'       : returned_user[0][0],
                    'username'      : returned_user[0][1],
                    'date_created'  : returned_user[0][2],
                    'num_sessions'  : returned_user[0][3]
                }
                return f(user_info)
                
        return make_response('Could not verify.', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
    return decorated
 
@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>INDEX EMPTY</h1>'

@app.route('/login', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POSTS'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_id = hash256_login(username, password)
        returned_user = get_user(user_id)

        if returned_user:
            user_info = {
                'user_id'       : returned_user[0][0],
                'username'      : returned_user[0][1],
                'date_created'  : returned_user[0][2],
                'num_sessions'  : returned_user[0][3]
            }

    return render_template('register.html')

@app.route('/profile')
@authorize
def profile(user):
    '''
    content = {
        'username' = user[0][0]
    }
    '''
    return render_template('profile.html', user=user)



if __name__ == '__main__':
    app.run(debug=True)