#using activated venv, so no shebang
import os
import unittest

from app import create_test_app
from models import User, Student, Group, Mentor, Session, SessionAction, Payment
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

    def test_SessionActions1(self):
        u1 = User(username='Han')
        u2 = User(username='Leia')

        g1 = Group(name='Solo')

        s1 = Student(name='Ray')
        s2 = Student(name='Kylo')

        sesh1 = Session()
        sesh2 = Session()

        seshA1 = SessionAction(type='moved')
        seshA2 = SessionAction(type='confirmed')

        db.session.add(u1)
        db.session.add(u2)
        db.session.add(g1)
        db.session.add(s1)
        db.session.add(s2)
        db.session.add(sesh1)
        db.session.add(sesh2)
        db.session.add(seshA1)
        db.session.add(seshA2)
        db.session.commit()

        g1.add_student(s1)
        g1.add_student(s2)

        g1.add_session(sesh1)
        g1.add_session(sesh2)

        seshA1.user_id = u1.id
        seshA2.user_id = u2.id
        sesh1.add_SessionAction(seshA1)
        sesh2.add_SessionAction(seshA2)

        assert sesh2.has_SessionAction(seshA2)
        assert sesh1.has_SessionAction(seshA1)


    def test_payments_users(self):
        u1 = User(username='Han')
        u2 = User(username='Leia')

        p1 = Payment(total = 400)
        p2 = Payment(total = 600)

        db.session.add(u1)
        db.session.add(u2)
        db.session.add(p1)
        db.session.add(p2)
        db.session.commit()

        u1.add_payment(p1)
        u2.add_payment(p2)

        assert u1.has_payment(p1)
        assert u2.has_payment(p2)
        assert p1.payer_id == u1.id
        assert p2.payer_id == u2.id





        


    






if __name__ == '__main__':
    unittest.main()