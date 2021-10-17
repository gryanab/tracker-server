import psycopg2

def create_table():
    conn = psycopg2.connect(
        "dbname='tracker' user='postgres' host='localhost' port='5555'")
    cur = conn.cursor()
    cur.execute(
        "CREATE TYPE GENDER_TYPE AS ENUM ('MALE', 'FEMALE')"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS profiles (user_id uuid NOT NULL, name TEXT NOT NULL UNIQUE, birthdate TIMESTAMP DEFAULT NOW(), gender GENDER_TYPE, CONSTRAINT pkey_profile PRIMARY KEY ( user_id ));"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS accounts (user_id uuid NOT NULL, email TEXT, password TEXT);"
    )
    cur.execute(
        "CREATE TYPE RUN_TYPE AS ENUM ('TRAINING', 'COMPETITION')"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS runs (user_id uuid NOT NULL, type RUN_TYPE NOT NULL, distance INT NOT NULL, time DECIMAL NOT NULL)"
    )
    conn.commit()
    conn.close()

create_table()
