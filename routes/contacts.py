
from flask import Blueprint, redirect, render_template, request, url_for, flash
from models.contact import Contact
from utils.db import db

contacts=Blueprint('contacts',__name__)

#Mostrar interfaz con contactos y formulario
@contacts.route('/')
def home():
    contactslist=Contact.query.all()
    return render_template('index.html', contacts=contactslist)

#Agregar contacto
@contacts.route('/new', methods=['POST'])
def add_contact():
    fullname=request.form['fullname']
    email=request.form['email']
    phone=request.form['phone']

    new_contact=Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()
    flash('Contact added successfully')
    return redirect(url_for('contacts.home'))

@contacts.route('/update/<id>', methods=['POST', 'GET'])
def update_contact(id):
    contactupd=Contact.query.get(id)
    if(request.method=='POST'):
        contactupd.fullname=request.form['fullname']
        contactupd.email=request.form['email']
        contactupd.phone=request.form['phone']
        db.session.commit()
        flash('Contact updated successfully')
        return redirect(url_for('contacts.home'))
    else:
        return render_template('update.html', contupd=contactupd)

@contacts.route('/delete/<id>')
def delete_contact(id):
    contactdel=Contact.query.get(id)
    db.session.delete(contactdel)
    db.session.commit()
    flash('Contact deleted successfully')
    return redirect(url_for('contacts.home'))

@contacts.route('/about')
def about():
    return render_template('about.html')