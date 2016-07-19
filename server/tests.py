#using activated venv, so no shebang
import os
import unittest

from app import create_test_app
from models import User, Student
from flask.ext.sqlalchemy import SQLAlchemy

app = create_test_app()
db = SQLAlchemy(app)

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_pop(self):
        u = User(username='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()

    def test_many_to_many(self):
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='kylo',email='k@starkillerbase.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        s1 = Student(name='Fin')
        s2 = Student(name='Ray')
        db.session.add(s1)
        db.session.add(s2)
        db.session.commit()

        u1.add_student(s1)
        u1.add_student(s2)

        assert u1.has_student(s1)
        assert u1.has_student(s2)





if __name__ == '__main__':
    unittest.main()