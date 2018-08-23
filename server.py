from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import os

app = Flask(__name__, template_folder= os.path.join(os.getcwd(), 'templates/'))
api = Api(app)

"""
Templates
"""

@app.route('/')
def index():
    return render_template('index.html')


users = [
    {
        "name": "Dre",
        "age": 20,
        "occupation": "EECS"
    },
    {
        "name": "Tina",
        "age": 20,
        "occupation": "Art History"
    },
    {
        "name": "Everett",
        "age": 20,
        "occupation": "Anthropology"
    }
]

class User(Resource):

    def get(self, name):
        for user in users:
            if (name == user["name"]):
                return user, 200
            return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                return "User with name {} already exists".format(name), 400
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }

        users.append(users)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted".format(name), 200

api.add_resource(User, "/user/<string:name>")

app.run(debug=True, port=8000)