import email
from operator import imod
from utils.db import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(10), nullable=False)

    def __init__(self, fullname, email, phone):
        self.fullname=fullname
        self.email=email
        self.phone=phone