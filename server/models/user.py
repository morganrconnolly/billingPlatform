from app import db


class User(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	email = db.Column(db.String(120))
	admin = db.Column(db.Boolean, default=False)
	students = db.relationship('Student', backref='parent', lazy='dynamic')

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