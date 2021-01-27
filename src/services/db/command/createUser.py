import psycopg2
import uuid
from flask import request
import psycopg2.extras

psycopg2.extras.register_uuid()


def create_user():
    userId = uuid.uuid4()
    content = request.json
    username = content['username']
    username_formatted = username.capitalize()
    conn = psycopg2.connect(
        "dbname='tracker' user='postgres' host='localhost' port='5555'")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO profile(name, userid) VALUES(%s, %s)", (username_formatted,
                                                             userId)
    )
    conn.commit()
    conn.close()
