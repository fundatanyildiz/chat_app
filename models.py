from sqlalchemy import Column, String, Integer
from main import db, app
from marshmallow import Schema, fields
from flask_login import UserMixin


# UserMixin allows to use methods like is_authenticated(),
# is_active(), get_id() and is_anonymous()
class Users(UserMixin, db.Model):
    __table_name__ = 'users'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String, nullable=False, unique=True)
    password = Column(String)


class UsersSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    surname = fields.String()
    email = fields.String()
    password = fields.String()


users_schema = UsersSchema(many=True)
user_schema = UsersSchema()


if __name__ == "__main__":
    # Run this file directly to create the database tables.
    # db.create_all uses db.engine which requires an active Flask app context.
    app.app_context().push()
    print("Creating database tables")
    db.create_all()
    print("Done!")
