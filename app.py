from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy

#Creando la instancia de flask
app = Flask(__name__)

#Configuración de SQLALCHEMY: root:12345@localhost:3306/nombredebasededatos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost:3306/contactsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SQLALCHEMY interpreta la configuración que se le colocó a la app
SQLAlchemy(app)

#Registrando el blueprint en la app
app.register_blueprint(contacts)