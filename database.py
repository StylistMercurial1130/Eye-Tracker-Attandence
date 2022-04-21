# database server code

import psycopg2

student_table_creation = """
    
    create table student(
        name        varchar(100),
        student_id  varchar(100),
        mail_id     varchar(100) PRIMARY KEY,
        password    varchar(100),
        course_id   varchar(100)[],
        course_name varchar(100)[]
    );
"""
teacher_table_creation = """
    create table teacher(
        name        varchar(100) ,
        teacher_id  varchar(100) ,
        course_name varchar(100)[],
        course_id   varchar(100)[],
        mail_id     varchar(100) PRIMARY KEY,
        password    varchar(100)
    );
"""

# add column for each courses ! when done with eye tracking !

class_table_creation = """
    create table class(
        student_id varchar(100),
        mail_id varchar(100) PRIMARY KEY,
        _19ELC311 float(20),
        _19ELC312 float(20),
        _19ELC313 float(20),
        _19ELC381 float(20),
        _CIR_ELC_2022 float(20),
        _19LAW300 float(20),
        _19CSE366 float(20),
        _19CSE448 float(20),
        _21ECE431 float(20),
        _19EEE335 float(20),
        _19EEE434 float(20) 
    );
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
        print("TEACHER TABLE CREATED !")

    if 'class' not in table_list : 
        cur.execute(class_table_creation)
        print("CLASS TABLE CREATED !")

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

    print("SUCCEFULLY CONNECTED TO DATABSE " + database_name)

    return conn

def response(request : str,db_conn) : 

    cur = db_conn.cursor()
    values = cur.execute(request)
    values = cur.fetchall()

    return values