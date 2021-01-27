import psycopg2
from flask import request


def set_gender(userId):
    content = request.json
    gender = content['gender']
    conn = psycopg2.connect(
        "dbname='tracker' user='postgres' host='localhost' port='5555'")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE profile SET gender=(%s)"
        "WHERE userid = (%s)",
        (gender, userId,))
    conn.commit()
    conn.close()
