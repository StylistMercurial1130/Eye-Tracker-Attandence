import enum
from unittest import result
from database import *
from utils import pass_inp
from utils import register_courses, teach_course
import hashlib
from commands import *

def stu_check_credentials(db_conn,mailid, password):
    # Code to retrieve password corresponding to the mail id
    # If the password matches the one in database, return True else False
    # If the mail id doesn't exist in the database, return -1
    password = hashlib.md5(password.encode())

    query = build_select_query(
        credentials_type.PASSWORD,
        "student",
        "mail_id = '{}'".format(mailid)
    )

    print("yay it works ! : " + query)

    result = response(query,db_conn)

    print(result)

    if not result:
        return -1


    if result[0] != password:
        return False

    return True

def teach_check_credentials(db_conn,mailid, password):
    # Code to retrieve password corresponding to the mail id
    # If the password matches the one in database, return True else False
    # If the mail id doesn't exist in the database, return -1

    password = hashlib.md5(password.encode())
    query = "select password from teacher where mail_id = " + mailid + " ;"

    db_conn.cursor().execute(query=query)

    result = db_conn.cursor().fetchall()

    if not result:
        return -1

    fixed_result = []

    for value in result : 
        fixed_result.append(list(map(str,list(value))))

    res = fixed_result[0][0]

    if res != password:
        return False

    return True

def stu_courses_registered(db_conn,mailid):
    # Code to retrieve courses registered by the student with this mail id  
    # return course as a list or a dictionary with the course id as the key and course name as the value

    query = "select course_id from student where " + "mail_id = " + mailid + ";"

    db_conn.cursor().execute(query=query)

    courses = db_conn.cursor().fetchall()

    return courses

def teach_courses_registered(db_conn,mailid):
    # Code to retrieve courses registered by the student with this mail id
    # return course as a list or a dictionary with the course id as the key and course name as the value
    
    query = "select course_id from teacher where " + "mail_id = " + mailid + ";"
   
    db_conn.cursor().execute(query=query)

    courses = db_conn.cursor().fetchall()
    
    return courses



def join_class(db_conn,mailid, courseid):
    # Put in an infinite loop until the student logs out of the class
    # track the eyes and update the attendance in the database
    # eye status is a variable that has either true or false 
    # true: the student is looking at the camera
    # false: the student is not looking at the camera




    class_status_polling = True

    while class_status_polling:
        print("something happens !")

    eye_status = True 

    # DB part
    # code to update the attendance of the student for the corresponding course in the database

def get_attendance(db_conn,courseid):
    # get the data of the students' attendance for the given course id
    # make a csv file of all the data 
    # save the csv file based on the path chosen by the user
    # return the path of the csv location
    path = 'C:\\Users\\User\\Desktop\\<courseid>_attendance.csv'
    return path

def stu_register():
    name = input("Enter your name : ")
    mailid = input('Enter your email id: ')
    password = pass_inp(f'Enter the password: ', 'passw')['passw']
    password = hashlib.md5(password.encode())

    student_id = input('Enter your student id: ')
    courses = register_courses() # returns a list of selected courses

    cur = db_conn.cursor()
    values = cur.execute("select mail_id from student")
    values = cur.fetchall()

    values = [i[0] for i in values]

    if mailid in values:
        return -1

    print(values)

    courses = courses.replace(" ","")
    courses = courses.split(",")

    courses_string = ""

    for course in courses : 
        courses_string += "'{}',".format(course)

    courses_string.strip(',')

    insert_query = """
        insert into student values
        ('{}',{},ARRAY[{}],{},{})
    """.format(name,student_id,mailid,password,courses_string, ) # TODO: NEEDS REWORKING

    db_conn.cursor().execute(insert_query)
    db_conn.cursor().execute("select student_id from student;")

    values = db_conn.cursor().fetchall()

    if student_id in values:
        return 1

    return 0
    # Check if the mail id already exists in the database
    # If the data doesn't exist add an entry to the corresponding table
    # On successful creation of the entry, return 1
    # If the mail id already exists in the database, return -1

def teach_register(db_conn):

    name = input("Enter your name : ")
    mailid = input('Enter your email id: ')
    password = pass_inp(f'Enter the password: ', 'passw')['passw']
    password = hashlib.md5(password.encode())

    teacher_id = input('Enter your roll teacher id: ')
    courses = teach_course() # returns a list of selected courses

    db_conn.cursor().execute("select mail_id from student")

    values = db_conn.cursor().fetchall()

    if mailid in values:
        return -1

    
    courses = courses.replace(" ","")
    courses = courses.split(",")

    courses_string = ""

    for course in courses : 
        courses_string += "'{}',".format(course)

    courses_string.strip(',')


    insert_query = """
        insert into teacher values
        ('{}',{},ARRAY[{}],{},{})
    """.format(teacher_id,name,courses_string,mailid,password) # NEEDS REWORKING, YEAH that shit is not working

    db_conn.cursor().execute(insert_query)
    db_conn.cursor().execute("select teacher_id from teacher;")

    values = db_conn.cursor().fetchall()

    if teacher_id in values:
        return 1

    return 0

    # Check if the mail id already exists in the database
    # If the data doesn't exist add an entry to the corresponding table
    # On successful creation of the entry, return 1
    # If the mail id already exists in the database, return -1

#TODO: prompt an attendance threshold for teachers