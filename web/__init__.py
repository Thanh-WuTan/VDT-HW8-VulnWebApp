from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask import session 
from flask_session import Session

db = SQLAlchemy()
DB_NAME = "database.db"

base_dir = os.path.dirname(__file__) + '/../'
template_path = os.path.join(base_dir, 'templates')


SESSION_TYPE = 'filesystem'

def create_app():
    app = Flask(__name__, template_folder=template_path)
    app.config['SECRET_KEY'] = 'my super secret key that no one is supposed to know'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
    app.config["SESSION_TYPE"] = SESSION_TYPE
    sess = Session(app)
    sess.init_app(app)
    
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
    