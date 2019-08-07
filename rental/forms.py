from wtforms import Form, StringField, SubmitField, validators
from wtforms.validators import input_required, Email
from flask_wtf import FlaskForm

class Newsletterform(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    email = StringField("Email", validators = [Email])
    submit = SubmitField()

class ContactForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    email = StringField("Email", validators = [Email])
    subject = StringField("subject")
    message = StringField("message")
    submit = SubmitField()
