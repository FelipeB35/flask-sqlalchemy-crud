from flask import Blueprint, render_template, request, redirect
from models.contact import Contact
from utils.db import db

#Guardando las rutas en un blueprint
contacts = Blueprint('contacts', __name__)


#Creación de cada ruta:

@contacts.route('/')
def home():
    return render_template('index.html')

@contacts.route('/new', methods = ['POST'])
def add_contact():
    #Extrayendo datos del form y guardandolos en una variable
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    
    #Usando la funcion de model para introducir valores en la columna correspondiente
    new_contact = Contact(fullname, email, phone)
    
    #Añadiendo los valores a la tabla en la bd
    db.session.add(new_contact)
    db.session.commit()
    
    return redirect('/')

@contacts.route('/update')
def update():
    return "Updating a contact"

@contacts.route('/delete')
def delete():
    return "Deleting a contact"

@contacts.route('/about')
def about():
    return render_template('about.html')
