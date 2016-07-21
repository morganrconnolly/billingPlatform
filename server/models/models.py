from app import db
from datetime import datetime

#association table for User/Student many-to-many relationship
students = db.Table('students',
    db.Column('parent_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'))
)

class Group(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	isActive = db.Column(db.Boolean, default=True)

	#many-to-one relationship with Mentor
	mentor_id = db.Column(db.Integer, 
							db.ForeignKey('mentor.id'))

	#one-to-many relationship with Student
	students = db.relationship('Student',
								backref='group',
								lazy='dynamic')

	#one-to-many relationship with Session
	sessions = db.relationship('Session',
								backref='group',
								lazy='dynamic')


	def add_student(self,student):
		if not self.has_student(student):
			self.students.append(student)
			return self

	def has_student(self,student):
		return self.students.filter(student.id==student.id).count() > 0

	def has_session(self, session):
		return self.sessions.filter(session.id==session.id).count() > 0

	def add_session(self, session):
		if not self.has_session(session):
			self.sessions.append(session)
			return self





class User(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	email = db.Column(db.String(120))
	admin = db.Column(db.Boolean, default=False)
	deleted = db.Column(db.Boolean, default=False)

	#many-to-many relationship with students
	students = db.relationship('Student', 
								secondary=students,
								primaryjoin=(students.c.parent_id==id),
								lazy='dynamic')

	#one-to-many relationship with SessionAction
	sessionActions = db.relationship('SessionAction',
										backref='user',
										lazy='dynamic')

	#one-to-many relationship with Payment
	payments = db.relationship('Payment',
									backref='payer',
									lazy = 'dynamic')

	#many-to-one relationship with Family
	family_id = db.Column(db.Integer,
						db.ForeignKey('family.id'))

	def add_student(self, student):
		if not self.has_student(student):
			self.students.append(student)
			return self

	def has_student(self, student):
		return self.students.filter(students.c.student_id==student.id).count() > 0


	def add_payment(self, payment):
		if not self.has_payment(payment):
			self.payments.append(payment)

	def has_payment(self, payment):
		return self.payments.filter(payment.id==payment.id).count() > 0


	

	#the below properties are expected by the flask-login module
	@property 
	def is_authenticated(self):
		return True
	@property 
	def is_active(self):
		return True

	@property 
	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id) #python 2
		except NameError:
			return str(self.id) #python 3

	def get_students(self):
		return self.students

	def __repr__(self):
		return '<User %r>' % (self.nickname)


class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	studentQ = db.Column(db.String(64), index=True)
	deleted = db.Column(db.Boolean, default=False)
	#many-to-many relationship with Users
	parents = db.relationship('User',
							secondary=students,
							secondaryjoin=(students.c.student_id==id),
							lazy='dynamic')
	#many-to-one relationship with Group
	group_id = db.Column(db.Integer, 
							db.ForeignKey('group.id'))

	#one-to-many relationship with SessionCredit
	"""
	SessionCredits = db.relationship('SessionCredit',
										backref='student',
										lazy='dynamic')
	"""

	#many-to-one relationship with Family
	family_id = db.Column(db.Integer, 
							db.ForeignKey('family.id'))

	def has_parent(self, user):
		return self.parents.filter(students.c.parent_id==user.id).count() > 0

	def __repr__(self):
		return '<Student %r>' % (self.name)

class StudentRates(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	rate = db.Column(db.Integer)
	description = db.Column(db.String(120))

class Mentor(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120))
	isActive = db.Column(db.Boolean, default=True)
	email = db.Column(db.String(120))
	phone = db.Column(db.String(20))

	#one-to-many relationship with Group
	groups = db.relationship('Group',
								backref='mentor',
								lazy='dynamic')

	def has_group(self,group):
		return self.groups.filter(group.id==group.id).count() > 0

	def add_group(self,group):
		if not self.has_group(group):
			self.groups.append(group)
			return self

class Session(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
	DateTime = db.Column(db.DateTime)
	isCanceled = db.Column(db.Boolean, default=False)

	#one-to-many relationship with SessionAction
	SessionActions = db.relationship('SessionAction',
										backref='session',
										lazy = 'dynamic')

	#one-to-one relationship with SessionCredit
	SessionCredit = db.relationship('SessionCredit',
										backref='session',
										lazy = 'dynamic')

	def add_SessionAction(self, SessionAction):
		if not self.has_SessionAction(SessionAction):
			self.SessionActions.append(SessionAction)
			return self

	def has_SessionAction(self, SessionAction):
		return self.SessionActions.filter(SessionAction.id == SessionAction.id).count > 0

	#returns query object
	def get_SessionAction_type(self, type):
		return self.SessionActions.filter(SessionAction.Type == type)



class SessionAction(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	#many-to-one relationship with Session
	session_id = db.Column(db.Integer, 
							db.ForeignKey('session.id'))

	#many-to-one relationship with User
	user_id = db.Column(db.Integer,
						db.ForeignKey('user.id'))
	DateTime = db.Column(db.DateTime, default = datetime.utcnow)
	type = db.Column(db.String(24))
	MoveDetails= db.Column(db.String(120))


class Payment(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	total = db.Column(db.Integer)

	#one-to-many relationship with SessionCredit
	SessionCredits = db.relationship('SessionCredit',
							backref = 'payment',
							lazy = 'dynamic')
	DateTime = db.Column(db.DateTime)

	#many-to-one relationship with User
	payer_id = db.Column(db.Integer,
						db.ForeignKey('user.id'))

	details = db.Column(db.String(120))
	isRefunded = db.Column(db.Boolean, 
							default=False)

class SessionCredit(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	#many-to-one relationship with Payment
	payment_id = db.Column(db.Integer,
							db.ForeignKey('payment.id'))

	#one-to-one relationship with Session
	session_id = db.Column(db.Integer,
							db.ForeignKey('session.id'))


	#one-to-many relationship with Student
	#student_id = db.column(db.Integer,
							#db.ForeignKey('student.id'))



	DateTime = db.Column(db.DateTime)


class Family(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120))
	IDHash = db.Column(db.String(120))

	#one-to-many relationship with Student
	students = db.relationship('Student',
								backref='family',
								lazy='dynamic')

	#one-to-many relationship with User
	parents = db.relationship('User',
								backref='family',
								lazy='dynamic')












