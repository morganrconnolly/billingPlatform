from flask import Flask 
from flask.ext.restful import Api, Resource

api = Api(app)

#what file(s) is making calls to this API?

class UserAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')