from ..app import db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Enum, ForeignKey

class Gender(enum.Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'

class Run_type(enum.Enum):
    TRAINING = 'TRAINING'
    COMPETITION = 'COMPETITION'

class Profiles(db.Model):
    __tablename__ = 'profiles'
    user_id = db.Column(UUID(as_uuid=True), primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    gender = db.Column(Enum(Gender))
    birthdate = db.Column(db.TIMESTAMP(timezone=False))

class Accounts(db.Model):
    user_id = db.Column(UUID(as_uuid=True), ForeignKey('profiles.user_id'), primary_key=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(60), nullable=False)

class Runs(db.Model):
    run_type = db.Column(Enum(Run_type), nullable=False)
    distance = db.Column(db.Integer(), nullable=False)
    time = db.Column(db.Numeric(), nullable=False)
    run_id = db.Column(db.String(250), nullable=False, unique=True)
    
db.create_all()
