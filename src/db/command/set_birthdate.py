import psycopg2
from flask import request

from ..db_connect import db_connect


def set_birthdate(userId):
    content = request.json
    birthdate = content['birthdate']
    [conn, cursor] = db_connect()
    try:
        cursor.execute(
            "UPDATE profiles SET birthdate=(%s)"
            "WHERE user_id = (%s)",
            (birthdate, userId,))
    except Exception as e: raise ValueError('[DB]: ERROR WHILE SETTING BIRTHDATE', e)
    conn.commit()
    conn.close()
