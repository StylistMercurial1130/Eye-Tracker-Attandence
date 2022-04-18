# database server code
import sys
import psycopg2

def connect_to_databse(database_name,database_username,database_password) :

    conn = None

    try : 
        conn = psycopg2.connect(
            dbname = database_name,
            user = database_username,
            password = database_password
        )
    except psycopg2.OperationalError as e:
        print(e.args[0])
        return None

    return conn

connect_to_databse(None,"postgres","1234")

