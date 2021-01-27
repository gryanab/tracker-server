import psycopg2
from services.db.command.createUser import create_user
from services.db.command.setGender import set_gender
from services.db.command.setBirthdate import set_birthdate
from flask import Flask, request
app = Flask(__name__)


@app.route('/users/create', methods=['POST'])
def post_create_user():
    create_user()
    return 'User created succesfully'


@app.route('/users/<userId>/gender', methods=['PATCH'])
def patch_set_gender(userId):
    set_gender(userId)
    return 'Gender set succesfully'


@app.route('/users/<userId>/birthdate', methods=['PATCH'])
def patch_set_birthdate(userId):
    set_birthdate(userId)
    return 'Birthdate set succesfully'
