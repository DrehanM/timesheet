from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

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

    def put(self, name):

    def delete(self, name):