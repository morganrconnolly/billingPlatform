from app import db

class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	studentQ = db.Column(db.String(64), index=True)
	deleted = db.Column(db.Boolean, default=False)


	def __repr__(self):
		return '<Student %r>' % (self.name)