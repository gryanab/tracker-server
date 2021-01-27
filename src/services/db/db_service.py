import psycopg2


def create_table():
    conn = psycopg2.connect(
        "dbname='tracker' user='postgres' host='localhost' port='5555'")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS profile (userId uuid NOT NULL, name TEXT, birthdate DATE, gender TEXT, CONSTRAINT pkey_profile PRIMARY KEY ( userId ))"
    )
    conn.commit()
    conn.close()

# def insert_data(name, age, gender):
#     conn = psycopg2.connect(
#         "dbname='tracker' user='postgres' host='localhost' port='5555'")
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO profile VALUES(%s,%s,%s)", (name, age, gender)
#     )
#     conn.commit()
#     conn.close()


# def view():
#     conn = psycopg2.connect(
#         "dbname='tracker' user='postgres' host='localhost' port='5555'")
#     cur = conn.cursor()
#     cur.execute(
#         "SELECT * FROM profile")
#     rows = cur.fetchall()
#     conn.close()
#     return rows
