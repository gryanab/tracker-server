import psycopg2
from flask import request

from ..db_connect import db_connect


def get_profile(userId):
    [conn, cursor] = db_connect()
    try:
        cursor.execute("SELECT * FROM profiles WHERE user_id = (%s) ", (userId,))
        results = cursor.fetchone()
        names = ['userId', 'userName', 'gender', 'birthdate']
    except Exception as e: raise ValueError('[DB]: ERROR WHILE GETTING ALL PROFILES', e)
    conn.commit()
    conn.close()
    return dict(zip(names, results))