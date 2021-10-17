from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
from flask_migrate import Migrate

from db.command.create_user import create_user
from db.command.set_gender import set_gender
from db.command.set_birthdate import set_birthdate
from db.command.create_run import create_run
from db.command.set_run import set_run

from db.query.get_all_profiles import get_all_profiles as get_all_profiles_qry
from db.query.get_profile import get_profile as get_profile_qry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Pikey,1863@localhost:5555/tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.create_all()


users_prefix = '/users/'

@app.route('{}create'.format(users_prefix), methods=['POST'])
def post_create_user():
    create_user()
    return 'User created succesfully'
  
@app.route('{}<userId>/gender'.format(users_prefix), methods=['PATCH'])
def patch_set_gender(userId):
    set_gender(userId)
    return 'Gender set succesfully'

@app.route('{}<userId>/birthdate'.format(users_prefix), methods=['PATCH'])
def patch_set_birthdate(userId):
    set_birthdate(userId)
    return 'Birthdate set succesfully'

@app.route('{}all'.format(users_prefix), methods=['GET'])
def get_all_profiles():
    profiles = get_all_profiles_qry()
    return jsonify(profiles)

@app.route('{}one/<userId>'.format(users_prefix), methods=['GET'])
def get_profile(userId):
    profile = get_profile_qry(userId)
    return profile

@app.route('{}run/<userId>'.format(users_prefix), methods=['POST'])
def post_create_run(userId):
    create_run(userId)
    return 'Run set successfully'

@app.route('{}run/<runId>'.format(users_prefix), methods=['PATCH'])
def patch_set_run(runId):
    set_run(runId)
    return 'Run updated successfully'