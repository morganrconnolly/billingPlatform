from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from models import User
from app import db, app

users_api = Api(Blueprint('users_api', __name__))

@users_api.resource('/users')
class UsersAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type = str, required = True,
            help = 'No username provided', location = 'json')
        super(UsersAPI, self).__init__()


    @staticmethod
    def get():
        users = User.query
        return [{
            'username':user.username,
            'id': user.id,
            'email': user.email
        } for user in users]

    #need to figure out how to pass arguments into url to create new user
    def post():
        args = self.reqparse.parse_args()
        user = User(username=args['username'])
        db.session.add(user)
        db.session.commit()