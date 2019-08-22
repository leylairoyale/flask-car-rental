from flask import render_template, redirect, url_for
from rental import app
from rental.forms import Newsletterform, ContactForm
from rental.models import db, Newsletter, Contact

@app.route("/")
def go_home():
    return render_template("home.html")

@app.route("/newsletter", methods=["GET", "POST"])
def get_newsletter():
    form = Newsletterform()
    first_name = form.first_name.data
    last_name = form.last_name.data
    email = form.email.data
    newsing = Newsletter(first_name, last_name, email)
    if form.validate_on_submit:
        db.session.add(newsing)
        db.session.commit()
    return render_template("newsletter.html")

@app.route("/contact", methods=["GET", "POST"])
def contactus():
    form = ContactForm()
    first_name = form.first_name.data
    last_name = form.last_name.data
    email = form.email.data
    subject = form.subject.data
    message = form.message.data
    contacting = Contact(first_name, last_name, email, subject, message)
    db.session.add(contacting)
    db.session.commit()
    return render_template("contact.html", form=form)