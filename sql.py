from database import *
from utils import clear_screen, pass_inp
from utils import register_courses, teach_course
import hashlib
from gaze_tracking import GazeTracking
import cv2 , csv , time , keyboard 
import tkinter as tk
from tkinter import filedialog


def stu_check_credentials(db_conn,mailid, password):
    ''' 
    Code to retrieve password corresponding to the mail id
    If the password matches the one in database, return True else False
    If the mail id doesn't exist in the database, return -1
    '''
    
    password = hashlib.md5(password.encode()).hexdigest()

    query = "select mail_id , password from student where mail_id = " + "'{}'".format(mailid) + ";"

    result = response(query,db_conn)
    if(len(result) == 0):
        return -1
    result = result[0]

    if result[1] != password:
        return False

    return True

def teach_check_credentials(db_conn,mailid, password):
    '''
    Code to retrieve password corresponding to the mail id
    If the password matches the one in database, return True else False
    If the mail id doesn't exist in the database, return -1
    '''

    password = hashlib.md5(password.encode()).hexdigest()
        
    query = "select mail_id , password from teacher where mail_id = " + "'{}'".format(mailid) + ";"

    result = response(query,db_conn)

    if(len(result) == 0):
        return -1
    result = result[0]

    if result[1] != password:
        return False

    return True

def stu_courses_registered(db_conn,mailid):
    '''
    Code to retrieve courses registered by the student with this mail id  
    return course as a list or a dictionary with the course id as the key and course name as the value
    '''

    query = "select course_id, course_name from student where " + "mail_id = " + "'{}'".format(mailid) + ";"

    result = response(query,db_conn)

    if len(result) == 0:
        return -1

    result = [result[0][0][i]+' - '+result[0][1][i] for i in range(len(result[0][1]))]

    return result

def teach_courses_registered(db_conn,mailid):
    '''
    Code to retrieve courses registered by the student with this mail id
    return course as a list or a dictionary with the course id as the key and course name as the value
    '''
    
    query = "select course_id, course_name from teacher where " + "mail_id = '" + mailid + "';"
   
    result = response(query,db_conn)

    result = [result[0][0][i]+' - '+result[0][1][i] for i in range(len(result[0][1]))]

    return result

def join_class(db_conn,mailid, courseid):
    '''
    Put in an infinite loop until the student logs out of the class
    track the eyes and update the attendance in the database
    eye status is a variable that has either true or false 
    true: the student is looking at the camera
    false: the student is not looking at the camera
    '''

    class_status_polling = True
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0)
    attendance = 0
        
    while class_status_polling:

        _, frame = webcam.read()
        try:
            gaze.refresh(frame)
        except:
            continue
        
        cv2.putText(frame, f"Current attendance: {attendance}s", (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)
        cv2.imshow(courseid, frame)
        
        if gaze.is_center() or gaze.is_blinking():
            
            attendance += 1
            clear_screen()

            print("press 'q' to end the class")
            print(f'current attendance for this session: {attendance}s')
            
            time.sleep(0.1)

        if keyboard.is_pressed("q") or cv2.waitKey(1) == 27 or 0xFF == ord('q'):
            
            print("q pressed, ending loop")
            
            query = f"update class set _{courseid} = _{courseid} + {attendance/60} where mail_id = '{mailid}';"
            cur = db_conn.cursor()
            cur.execute(query)
            class_status_polling = False
            
            return

def get_path_popup():

    root = tk.Tk() # create a tkinter object
    root.attributes('-topmost',1)
    root.withdraw() # close the pop up created by tkinter

    file_path = filedialog.askdirectory(
        title = 'Select the directory') # select a directory
    
    return file_path

def get_attendance(db_conn,courseid):
    '''
    get the data of the students' attendance for the given course id
    make a csv file of all the data 
    save the csv file based on the path chosen by the user
    return the path of the csv location
    '''

    values = response(f"""select 
                            s.name , c.student_id , c.mail_id , c._{courseid} 
                          from 
                            student s, class c 
                           where 
                            c.mail_id = s.mail_id;""",
                        db_conn)

    thres = float(input('Enter a threshold attendance percentage: '))
    total = float(input('Enter the total time of the classes taken: '))

    fields = ['Name', 'Student ID', 'Student Mail ID', courseid, 'Attendance (mins)', 'Min. attendance']

    rows = [list(i) for i in values]

    # Add minimum attendance column
    for i in rows:
        perc = (i[3]/total) * 100
        if perc > thres:
            i.append(True)
        else:
            i.append(False)
    
    sel_path = get_path_popup()

    while sel_path == '':
        clear_screen()
        print('Valid path not selected. Select a directory.')
        sel_path = get_path_popup()
    
    sel_path = sel_path + f"/{courseid}_attendance.csv"

    with open(sel_path, 'w') as csvfile: 

        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
            
        # writing the fields 
        csvwriter.writerow(fields) 
            
        # writing the data rows 
        csvwriter.writerows(rows)

    return sel_path

def stu_register(db_conn):
    '''
    Check if the mail id already exists in the database
    If the data doesn't exist add an entry to the corresponding table
    On successful creation of the entry, return 1
    If the mail id already exists in the database, return -1
    '''

    name = input("Enter your name : ")
    mailid = input('Enter your email id: ')
    password = pass_inp(f'Enter the password: ', 'passw')['passw']
    password = hashlib.md5(password.encode()).hexdigest()

    cur = db_conn.cursor()
    values = cur.execute("select mail_id from student")
    values = cur.fetchall()

    values = [i[0] for i in values]

    if mailid in values:
        print("it exists already !")
        return -1

    student_id = input('Enter your student id: ')
    courses = register_courses()

    insert_query = f"""
        insert into student values
        ('{name}','{student_id}','{mailid}','{password}',ARRAY[{', '.join("'"+item.strip()+"'" for item in courses.keys())}],ARRAY[{', '.join("'"+item.strip()+"'" for item in courses.values())}])
    """

    cur.execute(insert_query)

    cur.execute(f"insert into class values ('{student_id}','{mailid}', 0,0,0,0,0,0,0,0,0,0,0)")

    return 1    

def teach_register(db_conn):

    '''
    Check if the mail id already exists in the database
    If the data doesn't exist add an entry to the corresponding table
    On successful creation of the entry, return 1
    If the mail id already exists in the database, return -1
    '''

    name = input("Enter your name : ")
    mailid = input('Enter your email id: ')
    password = pass_inp(f'Enter the password: ', 'passw')['passw']
    password = hashlib.md5(password.encode()).hexdigest()

    cur = db_conn.cursor()
    values = cur.execute("select mail_id from teacher")
    values = cur.fetchall()
    values = [i[0] for i in values]

    if mailid in values:
        print("it exists already !")
        return -1

    teacher_id = input('Enter your teacher id: ')
    courses = teach_course()
    while len(courses.keys()) == 0:
        clear_screen()
        print('Please choose atleast one course to teach')  
        courses = teach_course()

    insert_query = f"""
        insert into teacher values
        ('{name}','{teacher_id}',ARRAY[{', '.join("'"+item.strip()+"'" for item in courses.values())}],ARRAY[{', '.join("'"+item.strip()+"'" for item in courses.keys())}],'{mailid}','{password}')
    """

    cur.execute(insert_query)

    return 1