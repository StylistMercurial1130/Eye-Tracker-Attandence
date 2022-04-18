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

conn = connect_to_databse("theater","postgres","1234")
cursor = conn.cursor()

cursor.execute("select title from movie where star = 'Jackie Chn';")

values = cursor.fetchall()

if not values:
    print("its empty !")

fixed_value = []

for value in values : 
    fixed_value.append(list(map(str,list(value))))

print(fixed_value)
