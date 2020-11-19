import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'K\xa5r\x94\xc2"\x06\x14\'\xc1\xe4\xa6\r\x9f\x16\xf9z4hIR\x14g\x1c'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'realestate.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'vrmconstructionrealestate@gmail.com'
app.config['MAIL_PASSWORD'] = 'Google@123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


import models
import views