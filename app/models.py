from . import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column('firstname', db.String(50), nullable=False)
    lastName = db.Column('lastname', db.String(50), nullable=False)
    emailId = db.Column('emailid', db.String(50), nullable=False)

    def __repr__(self):
        return f'<Employee {self.firstName} {self.lastName}>'
