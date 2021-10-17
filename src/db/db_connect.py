import psycopg2

def db_connect():
    conn = psycopg2.connect(
        "dbname='tracker' user='postgres' host='localhost' port='5555'")
    cursor = conn.cursor()
    return [conn, cursor]