from sql import stu_check_credentials, stu_courses_registered, join_class, stu_register, teach_check_credentials, teach_courses_registered, get_attendance, teach_register
from utils import pass_inp, get_who, get_login_register, yn_prompt
# from PyInquirer.prompt import prompt


who = get_who()

if who == 'student':

    ch1 = get_login_register()

    if ch1 == 'login':

        mailid = input("Enter your college mail ID: ")
        password = pass_inp(f'Enter the password: ', 'passw')['passw']

        check_creds = stu_check_credentials(mailid, password)
        
        if check_creds:
            # retrieve the courses registered by the student with the mail id
            courses = '\n'.join(stu_courses_registered(mailid))
            print(courses)
            class_join = input('Enter the index number corresponding to course to join that class: ')
            class_join -= 1
            join_class(mailid, courses[class_join])
        
        elif not check_creds:
            print('Wrong credentials :(')
        
        elif check_creds == -1:
            
            yn = yn_prompt('Mail ID doesn\'t exist. Would you like to register? ','yn')['yn']
            # Call registration funtion
            
            if yn:
                d = stu_register()
                if d == 1:
                    print('Account registered successfully')
                elif d == -1:
                    print('Account already exists. Please login')
            
            else:
                print('Exiting.')
                quit()
    
    elif ch1 == 'register':
       
        d = stu_register()

        if d == 1:
            print('Account created successfully.')
        elif d == -1:
            print('Account already exists. Please login')

elif who == 'teacher':
    
    ch1 = get_login_register()

    if ch1 == 'login':

        mailid = input('Enter your college mail ID: ')
        password = pass_inp(f'Enter the password: ', 'passw')['passw']
        check_creds = teach_check_credentials(mailid, password)
        
        if check_creds:
            # retrieve the courses registered by the teacher for teaching
            courses = '\n'.join(teach_courses_registered(mailid))
            print(courses)
            attendance = input('Enter the index number corresponding to course for retrieving the attendance: ')
            attendance -= 1
            path = get_attendance(courses[attendance])

        elif not check_creds:
            print('Wrong credentials')

        elif check_creds == -1:

            yn = yn_prompt('Mail ID doesn\'t exist. Would you like to register? ','yn')['yn']

            if yn:

                d = teach_register()

                if d == 1:
                    print('Account registered successfully')

                elif d == -1:
                    print('Account already exists. Please login')

            else:
                print('Exiting.')
                quit()
    
    if ch1 == 'register':

        d = teach_register()

        if d == 1:
            print('Account created successfully')
        elif d == -1:
            print('Account already exists. please login')