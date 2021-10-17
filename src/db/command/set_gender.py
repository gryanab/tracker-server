import psycopg2
from flask import request

from ..db_connect import db_connect



def set_gender(userId):
    [conn, cursor] = db_connect()
    
    content = request.json
    gender = content['gender']
    try:
        cursor.execute(
            "UPDATE profiles SET gender=(%s)"
            "WHERE user_id = (%s)",
            (gender, userId,))
    except Exception as e: raise ValueError('[DB]: ERROR WHILE SETTING GENDER', e)
    conn.commit()
    conn.close()
