from flask_sqlalchemy import SQLAlchemy
from rental import app


db = SQLAlchemy(app)

class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50),)
    last_name = db.Column(db.String(50),)
    email = db.Column(db.String(50), unique=True)
    
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    def __repr__(self):
        return "{} {} signed up for the news".format(self.first_name, self.last_name)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    subject = db.Column(db.String(100))
    message = db.Column(db.String(500))

    def __init__(self, first_name, last_name, email, subject, message):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.subject = subject
        self.message = message

    
    def __repr__(self):
        return "{} {} wrote something called {}".format(self.first_name, self.last_name, self.subject)