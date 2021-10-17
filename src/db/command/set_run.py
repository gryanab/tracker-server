from flask import request
import psycopg2.extras
import uuid

from ..db_connect import db_connect

def set_run(run_id):
    [conn, cursor] = db_connect()
    
    content = request.json
    run_type = content['runType']
    distance = content['distance']
    time = content['time']

    try:
        cursor.execute(
            "UPDATE runs SET distance=(%s), type=(%s), time=(%s) WHERE run_id=(%s)",
             (distance, run_type, time, run_id)
        )
    except Exception as e: raise ValueError('[DB]: ERROR WHILE CREATING RUN', e)
    conn.commit()
    conn.close()