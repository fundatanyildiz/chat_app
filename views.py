from flask import request, jsonify
from main import app, db, check_email
from models import Users, users_schema, user_schema
from werkzeug.security import generate_password_hash

@app.route('/')
def hello_app():
    return jsonify(message='Hello from chat app')


@app.route('/sign-up', methods=["POST"])
def register():
    email = request.form['email']
    # email validation
    flag = check_email(email)
    if not flag:
        return jsonify(message='You enter an invalid email!'), 403
    while flag:
        # check if user already registered
        test_user = Users.query.filter_by(email=email).first()
        if test_user:
            return jsonify(message='User already registered!'), 409
            break
        else:
            # if not registered, continue the registration
            password = request.form['password']
            name = request.form['name']
            surname = request.form['surname']
            new_user = Users(name=name, surname=surname, email=email, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            user = user_schema.dump(new_user)
            return jsonify(message='New user '+user['name'] + ' ' + user['surname']+', registered!'), 201
            break


@app.route('/users', methods=["GET"])
def get_users():
    results = Users.query.all()
    users = users_schema.dump(results)
    return jsonify(users)


@app.route('/login', methods=["POST"])
def login():
    email = request.form['email']
    test = Users.query.filter_by(email=email).first()
    if test:
        return jsonify(message='fff!')
    else:
        return jsonify(message='The user ')

