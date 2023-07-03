from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import re
from flask_login import LoginManager


app = Flask(__name__)
username = os.environ['DB_USERNAME']
password = os.environ['DB_PASSWORD']
login_manager = LoginManager()
# Set up the SQLAlchemy Database
app.config["SECRET_KEY"] = os.environ['SECRET_KEY']
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://' + username + ':' + password + '@localhost/postgres'
db = SQLAlchemy(app)
# regex for email validation
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
login_manager.init_app(app)


def check_email(mail):
    if re.fullmatch(regex, mail):
        print('You enter a valid email!')
        return True
    else:
        print('You enter an invalid email!')
        return False


if __name__ == '__main__':
    # We need to make sure Flask knows about its views before we run
    # the app, so we import them. We could do it earlier, but there's
    # a risk that we may run into circular dependencies, so we do it at the
    # last minute here.

    from views import *

    app.run(debug=True)
