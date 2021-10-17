from flask import request
import psycopg2.extras
import uuid

from ..db_connect import db_connect

psycopg2.extras.register_uuid()


def create_run(user_id):
    [conn, cursor] = db_connect()
    # find a way to add uuid extension into postgres
    runId = '{}-{}'.format(user_id, uuid.uuid4())
    
    content = request.json
    run_type = content['runType']
    distance = content['distance']
    time = content['time']

    try:
        cursor.execute(
            "INSERT INTO runs(run_id, distance, type, time) VALUES(%s, %s, %s, %s)", (runId, distance, run_type, time)
        )
    except Exception as e: raise ValueError('[DB]: ERROR WHILE CREATING RUN', e)
    conn.commit()
    conn.close()