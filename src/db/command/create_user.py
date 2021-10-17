import psycopg2
from flask import request
import psycopg2.extras
import uuid

from ..db_connect import db_connect

psycopg2.extras.register_uuid()

def create_user():
    [conn, cursor] = db_connect()
    # find a way to add uuid extension into postgres
    userId = uuid.uuid4()
    
    content = request.json
    username = content['username']
    password = content['password']
    email = content['email']

    username_formatted = username.capitalize()
    try:
        cursor.execute(
            "INSERT INTO profiles(user_name, user_id) VALUES(%s, %s)", (username_formatted, userId)
        )
        cursor.execute(
            "INSERT INTO accounts(user_id, password, email) VALUES(%s, %s, %s)", (userId, password, email )
        )
    except Exception as e: raise ValueError('[DB]: ERROR WHILE CREATING USER', e)
    conn.commit()
    conn.close()
