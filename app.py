from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from apifairy import APIFairy

app = Flask(__name__)
# Configuration de la base de données (PostgreSQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/library_db'
app.config['APIFAIRY_TITLE'] = 'Library API'
app.config['APIFAIRY_VERSION'] = '1.0'

db = SQLAlchemy(app)
ma = Marshmallow(app)
af = APIFairy(app)

@app.route('/')
def index():
    return "L'API de la bibliothèque fonctionne !"

if __name__ == '__main__':
    app.run(debug=True)