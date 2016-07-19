from app import db

#association table for User/Student many-to-many relationship
students = db.Table('students',
    db.Column('parent_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'))
)


class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	studentQ = db.Column(db.String(64), index=True)
	deleted = db.Column(db.Boolean, default=False)
	parents = db.relationship('User',
							secondary=students,
							secondaryjoin=(students.c.student_id==id),
							lazy='dynamic')


	def __repr__(self):
		return '<Student %r>' % (self.name)



class User(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	email = db.Column(db.String(120))
	admin = db.Column(db.Boolean, default=False)
	students = db.relationship('Student', 
								secondary=students,
								primaryjoin=(students.c.parent_id==id),
								lazy='dynamic')
	deleted = db.Column(db.Boolean, default=False)

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

	def add_student(self, student):
		if not self.has_student(student):
			self.students.append(student)
			return self

	def has_student(self, student):
		return self.students.filter(students.c.student_id==student.id).count() > 0


	def get_id(self):
		try:
			return unicode(self.id) #python 2
		except NameError:
			return str(self.id) #python 3

	def get_students(self):
		return self.students

	def __repr__(self):
		return '<User %r>' % (self.nickname)