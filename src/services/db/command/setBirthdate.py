import psycopg2
from flask import request


def set_birthdate(userId):
    content = request.json
    birthdate = content['birthdate']
    conn = psycopg2.connect(
        "dbname='tracker' user='postgres' host='localhost' port='5555'")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE profile SET birthdate=(%s)"
        "WHERE userid = (%s)",
        (birthdate, userId,))
    conn.commit()
    conn.close()
