from flask import Blueprint, render_template

#Guardando las rutas en un blueprint
contacts = Blueprint('contacts', __name__)


#Creación de cada ruta:

@contacts.route('/')
def home():
    return render_template('index.html')

@contacts.route('/new')
def add_contact():
    return "Saving a contact"

@contacts.route('/update')
def update():
    return "Updating a contact"

@contacts.route('/delete')
def delete():
    return "Deleting a contact"

@contacts.route('/about')
def about():
    return render_template('about.html')
