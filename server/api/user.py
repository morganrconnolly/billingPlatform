from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from models import User
from app import create_app, db

app = create_app()
api = API(app)

"""
get UserAPI when have user.id argument. So, we need a UsersAPI to
deal with User related requests that do not have a specific user
associated with them. E.g. creating a new user.
"""
class UsersAPI(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('username', type = str, required = True,
			help = 'No username provided', location = 'json')
		super(TaskListAPI, self).__init__()

	def post(self):
		args = self.reqparse.parse_args()
		user = User(username=args['username'])
		db.session.add(user)
		db.session.commit()


class UserAPI(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('username', type = str, location = 'json')
		self.reqparse.add_argument('email', type = str, location = 'json')
		self.reqparse.add_argument('admin', type = bool, location = 'json')
		super(TaskAPI, self).__init__()


    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass




api.add_resource(UsersAPI, '/users', endpoint = 'users')
api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')
