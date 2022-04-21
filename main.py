from database import connect_to_databse
from picker import Picker
from sql import stu_check_credentials, stu_courses_registered, join_class, stu_register, teach_check_credentials, teach_courses_registered, get_attendance, teach_register
from utils import pass_inp, get_who, get_login_register, yn_prompt

def main():

    db_conn = connect_to_databse("attendence","postgres","1234")
    
    who = get_who()

    if who == 'student':

        ch1 = get_login_register()

        if ch1 == 'login':

            mailid = input("Enter your college mail ID: ")
            password = pass_inp(f'Enter the password: ', 'passw')['passw']

            check_creds = stu_check_credentials(db_conn,mailid, password)

            if check_creds == -1:

                yn = yn_prompt('Mail ID doesn\'t exist. Would you like to register? ','yn')['yn']
                # Call registration funtion

                if yn:
                    d = stu_register(db_conn)
                    if d == 1:
                        print('Account registered successfully')
                    elif d == -1:
                        print('Account already exists. Please login')

                else:
                    print('Exiting.')
                    quit()
                
            elif check_creds == True:

                # retrieve the courses registered by the student with the mail id
                courses = stu_courses_registered(db_conn,mailid)

                picker = Picker(
                    courses,
                    "Select your choice using arrow keys or press q to quit", 
                    indicator=" => ")

                picker.register_custom_handler(ord('q'), lambda picker: exit())
                picker.register_custom_handler(ord('Q'), lambda picker: exit())
                _,class_join = picker.start()
                
                join_class(db_conn,mailid, courses[class_join].split('-')[0].strip())
                print("classs has ended, you quit the class")

            elif not check_creds:
                print('Wrong credentials :(')

        elif ch1 == 'register':
        
            d = stu_register(db_conn)

            if d == 1:
                print('Account created successfully.')
            elif d == -1:
                print('Account already exists. Please login')

    elif who == 'teacher':

        ch1 = get_login_register()

        if ch1 == 'login':

            mailid = input('Enter your college mail ID: ')
            password = pass_inp(f'Enter the password: ', 'passw')['passw']
            check_creds = teach_check_credentials(db_conn,mailid, password)

            if check_creds == -1:

                yn = yn_prompt('Mail ID doesn\'t exist. Would you like to register? ','yn')['yn']

                if yn:

                    d = teach_register(db_conn)

                    if d == 1:
                        print('Account registered successfully')

                    elif d == -1:
                        print('Account already exists. Please login')

                else:
                    print('Exiting.')
                    quit()

            elif check_creds:
                # retrieve the courses registered by the teacher for teaching
                courses = teach_courses_registered(db_conn,mailid)

                picker = Picker(
                    courses,
                    "Select your choice using arrow keys or press q to quit", 
                    indicator=" => ")

                picker.register_custom_handler(ord('q'), lambda picker: exit())
                picker.register_custom_handler(ord('Q'), lambda picker: exit())
                _,attendance = picker.start()

                path = get_attendance(db_conn,courses[attendance].split('-')[0].strip())

                print(f"Attendance file saved at {path}")

            elif not check_creds:
                print('Wrong credentials')

        if ch1 == 'register':

            d = teach_register(db_conn)

            if d == 1:
                print('Account created successfully')
            elif d == -1:
                print('Account already exists. please login')


def drop_table() :
    db_conn = connect_to_databse(
        "attendence",
        "postgres",
        "1234"
    )
    cur = db_conn.cursor()
    cur.execute("drop table student , teacher , class;") 

def _main():
    
    db_conn = connect_to_databse(
        "attendence",
        "postgres",
        "1234"
    )

    stu_courses_registered(db_conn,"bob@gmail.com")

if __name__ == '__main__' :
    main()