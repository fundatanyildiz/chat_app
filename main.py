from flask import Flask, jsonify
import os
import re
from flask_login import LoginManager

username = os.environ['DB_USERNAME']
password = os.environ['DB_PASSWORD']
login_manager = LoginManager()
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def create_app():
    app = Flask(__name__)

    # config secret key for sessions
    app.config["SECRET_KEY"] = os.environ['SECRET_KEY']
    # Set up the SQLAlchemy Database
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://' + username + ':' + password + '@localhost/postgres'
    # regex for email validation
    login_manager.init_app(app)

    from views import hello_app

    return app


def check_email(mail):
    if re.fullmatch(regex, mail):
        print('You enter a valid email!')
        return True
    else:
        print('You enter an invalid email!')
        return False
