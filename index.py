from app import app
from utils.db import db

#Crea la base de datos, si es que no existe, cada vez que se ejecuta la app
with app.app_context():
  db.create_all()

if "__main__" == __name__:
  app.run(debug=True, use_reloader=False)
