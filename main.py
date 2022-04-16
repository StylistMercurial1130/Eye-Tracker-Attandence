from sql import stu_check_credentials, stu_courses_registered, join_class, stu_register, teach_check_credentials, teach_courses_registered, get_attendance, teach_register


who = input('Login as Student or Teacher')

if who.lower() in ['s','student']:

    ch1 = input('Login/Register')

    if ch1.lower() in ['login','l']:
        mailid = input("Enter your college mail ID")
        password = input("Enter the password")
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
            yn = input('mail id doesn\'t exist. would you like to register? (y/n) ')
            # Call registration funtion
            if yn.lower() == 'y':
                d = stu_register()
                if d == 1:
                    print('Account registered successfully')
                elif d == -1:
                    print('Account already exists. Please login')
            else:
                print('Exiting.')
                quit()
    
    elif ch1.lower() in ['register','r']:
        d = stu_register()
        if d == 1:
            print('Account created successfully.')
        elif d==-1:
            print('Account already exists. Please login')

elif who.lower() in ['t','teacher']:
    
    ch1 = input('Login/Register')

    if ch1.lower() in ['login','l']:
        mailid = input('Enter your college mail ID: ')
        password = input('Enter the password')
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
            yn = input('mail id doesn\'t exist. would you like to register? (y/n)')
            if yn.lower() == 'y':
                d = teach_register()
                if d == 1:
                    print('Account registered successfully')
                elif d == -1:
                    print('Account already exists. Please login')
            else:
                print('Exiting.')
                quit()
    
    if ch1.lower() in ['register','r']:
        d = teach_register()
        if d == 1:
            print('Account created successfully')
        elif d == -1:
            print('Account already exists. please login')