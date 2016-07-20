#using activated venv, so no shebang
import os
import unittest

from app import create_test_app
from models import User, Student, Group, Mentor, Session
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

    def test_parents_to_students(self):
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
        assert s1.has_parent(u1)

        u2.add_student(s1)
        assert s1.has_parent(u2)

    def test_mentor_to_group(self):
        m = Mentor(name='Snoke')

        g1 = Group(name='Solo')
        g2 = Group(name='Generals')

        s1 = Student(name='Ray')
        s2 = Student(name='Kylo')
        s3 = Student(name='Hux')


        db.session.add(m)
        db.session.add(g1)
        db.session.add(g2)
        db.session.add(s1)
        db.session.add(s2)
        db.session.add(s3)
        db.session.commit()

        g1.add_student(s1)
        g1.add_student(s2)
        g2.add_student(s3)

        m.add_group(g1)
        m.add_group(g2)
        
        assert g1.mentor.name == 'Snoke'
        assert m.has_group(g2)

    def test_session_to_group(self):
        m = Mentor(name='Snoke')

        g1 = Group(name='Solo')
        g2 = Group(name='Generals')

        s1 = Student(name='Ray')
        s2 = Student(name='Kylo')
        s3 = Student(name='Hux')


        db.session.add(m)
        db.session.add(g1)
        db.session.add(g2)
        db.session.add(s1)
        db.session.add(s2)
        db.session.add(s3)
        db.session.commit()

        sesh1 = Session()
        g1.add_session(sesh1)
        db.session.add(sesh1)
        db.session.commit()

        g1.add_student(s1)
        g1.add_student(s2)
        g2.add_student(s3)

        assert g1.has_session(sesh1)
        assert sesh1.group_id == g1.id

    def test_SessionActions(self):
        u1 = User('Han')
        u2 = User('Leia')

        sesh1 = Session()
        sesh2 = Session()

        seshA1 = SessionAction(type='moved')
        seshA2 = SessionAction(type='confirmed')

        


    






if __name__ == '__main__':
    unittest.main()