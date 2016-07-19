import os
from flask.ext.sqlalchemy import SQLAlchemy
from logging import StreamHandler
from sys import stdout
from flask import Flask


db = SQLAlchemy()

def create_app():
    from api.kittens import kittens_api
    from api.users   import users_api
    from views.index import index_view

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

    #this is a quick fix for local development
    #app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/users_dev"

    app.register_blueprint(kittens_api.blueprint, url_prefix='/api')
    app.register_blueprint(users_api.blueprint, url_prefix='/api2')
    app.register_blueprint(index_view)

    db.init_app(app)

    handler = StreamHandler(stdout)
    app.logger.addHandler(handler)
    return app


def create_test_app():
    from api.kittens import kittens_api
    from api.users import users_api
    from views.index import index_view
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/test_dev"

    app.register_blueprint(kittens_api.blueprint, url_prefix='/api')
    app.register_blueprint(users_api.blueprint, url_prefix='/api2')
    app.register_blueprint(index_view)

    db.init_app(app)

    with app.app_context():
        db.create_all
    return app, db
