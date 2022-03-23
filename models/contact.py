from utils.db import db

#Creando modelo de contacts, se extrae cada columna de la db con su respectivo tipo de dato
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    
    #Permite que cada vez que se ejecute se guarde cada valor de la consulta
    def __init__(self, fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone
        