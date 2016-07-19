#using activated venv, so no shebang
import os
import unittest

from app import create_test_app
from models import User
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TestCase(unittest.TestCase):
    def setUp(self):
        app = create_test_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_pop(self):
        u = User(username='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()



if __name__ == '__main__':
    unittest.main()