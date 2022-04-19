# database server code

# import sys
from operator import contains
from secrets import choice
import psycopg2


student_table_creation = """
    
    create table student(
        name        varchar(20),
        student_id  varchar(10) PRIMARY KEY,
        mail_id     varchar(20),
        password    varchar(10),
        course_id   varchar(30)[],
        course_name varchar(40)[]
    );
"""
teacher_table_creation = """
    create table teacher(
        name        varchar(20),
        teacher_id  varchar(10) PRIMARY KEY,
        mail_id     varchar(20),
        password    varchar(10),
        course_id   varchar(30)[],
        course_name varchar(40)[]
    );
"""

# add column for each courses !

class_table_creation = """
    create table class(
        student_id varchar(10) REFERENCES student(student_id),
        student_name varchar(10) REFERENCES student(name)    
    )
"""

def create_table(conn) :

    conn.autocommit = True
    cur = conn.cursor()

    table_list = cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    table_list = cur.fetchall()

    table_list = [i[0] for i in table_list]
    
    if 'student' not in table_list : 
        cur.execute(student_table_creation)
        print("STUDENT TABLE CREATED !")

    if 'teacher' not in table_list : 
        cur.execute(teacher_table_creation)
        print("TEACHER TABLE CREATER")

    print("ALL TABLES CREATED !")

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

    '''create a table here , might be usefull '''
    create_table(conn)

    return conn



connect_to_databse("attendence","postgres","1234")


# conn = connect_to_databse("theater","postgres","1234")
# cursor = conn.cursor()

# cursor.execute("select title from movie where star = 'Jackie Chn';")

# values = cursor.fetchall()

# if not values:
#     print("its empty !")

# fixed_value = []

# for value in values : 
#     fixed_value.append(list(map(str,list(value))))

# print(fixed_value)
