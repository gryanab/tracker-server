import psycopg2
from flask import request

from ..db_connect import db_connect


def get_all_profiles():
    [conn, cursor] = db_connect()
    try:
        cursor.execute("SELECT * FROM profiles")
        results = cursor.fetchall()
        
        profiles = []
        names = ['userId', 'userName', 'gender', 'birthdate']
        for result in results:
            profiles.append(dict(zip(names, result)))
    except Exception as e: raise ValueError('[DB]: ERROR WHILE GETTING ALL PROFILES', e)
    conn.commit()
    conn.close()
    return profiles