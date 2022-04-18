from ctypes import sizeof
from database import *


# Global databse_connection change arguments based on need !
# should we make this modular ? whatever the other bois and gorls think 
db_conn = connect_to_databse("attendence","postgres","1234")

def stu_check_credentials(mailid, password):
    # Code to retrieve password corresponding to the mail id
    # If the password matches the one in database, return True else False
    # If the mail id doesn't exist in the database, return -1

    query = "select password from student where mail_id = " + mailid + " ;"

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

def teach_check_credentials(mailid, password):
    # Code to retrieve password corresponding to the mail id
    # If the password matches the one in database, return True else False
    # If the mail id doesn't exist in the database, return -1
    
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

def stu_courses_registered(mailid):
    # Code to retrieve courses registered by the student with this mail id  
    # return course as a list or a dictionary with the course id as the key and course name as the value

    query = "select course_id from student where " + "mail_id = " + mailid + ";"

    db_conn.cursor().execute(query=query)

    courses = db_conn.cursor().fetchall()

    return courses

def teach_courses_registered(mailid):
    # Code to retrieve courses registered by the student with this mail id
    # return course as a list or a dictionary with the course id as the key and course name as the value
    
    
    query = "select course_id from teacher where " + "mail_id = " + mailid + ";"

    db_conn.cursor().execute(query=query)

    courses = db_conn.cursor().fetchall()
    
    return courses



def join_class(mailid, courseid):
    # Put in an infinite loop until the student logs out of the class
    # track the eyes and update the attendance in the database
    # eye status is a variable that has either true or false 
    # true: the student is looking at the camera
    # false: the student is not looking at the camera
    eye_status = True 

    # DB part
    # code to update the attendance of the student for the corresponding course in the database

def get_attendance(courseid):
    # get the data of the students' attendance for the given course id
    # make a csv file of all the data 
    # save the csv file based on the path chosen by the user
    # return the path of the csv location
    path = 'C:\\Users\\User\\Desktop\\<courseid>_attendance.csv'
    return path

def stu_register():
    mailid = input('Enter your email id: ')
    password = input('Enter a password: ')
    rollno = input('Enter your roll number: ')
    courses = input('Select the courses for the enrollment: ')

    

    # Check if the mail id already exists in the database
    # If the data doesn't exist add an entry to the corresponding table
    # On successful creation of the entry, return 1
    # If the mail id already exists in the database, return -1

def teach_register():
    mailid = input('Enter your email id: ')
    password = input('Enter a password: ')
    rollno = input('Enter your roll number: ')
    courses = input('Select the courses for the enrollment: ')

    # Check if the mail id already exists in the database
    # If the data doesn't exist add an entry to the corresponding table
    # On successful creation of the entry, return 1
    # If the mail id already exists in the database, return -1