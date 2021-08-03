from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__) # Creating Flask Object
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = str(os.urandom(16))



db = SQLAlchemy(app) # create SQLALchemy object