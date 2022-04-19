# database server code

# import sys
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

    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("drop table student , teacher , class;")  
    cur.execute(student_table_creation)
    cur.execute(teacher_table_creation)
    



    print(values)

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
