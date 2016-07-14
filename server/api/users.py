from flask import Blueprint
from flask_restful import Api, Resource
from models import User

users_api = Api(Blueprint('users_api', __name__))

@kittens_api.resource('/users')
class UsersAPI(Resource):
    @staticmethod
    def get():
        users = User.query
        return [{
            'username':user.username,
            'id': user.id,
            'email': user.email
        } for user in users]

    #need to figure out how to pass arguments into url to create new user
    @staticmethod
    def post():
        from app import db

        pass