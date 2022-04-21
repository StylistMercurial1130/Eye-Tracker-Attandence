import sys,os
from PyInquirer.prompt import prompt
from PyInquirer import Separator

def clear_screen():
    if sys.platform=='win32' or os.name=='nt':
        os.system("cls")
    elif sys.platform=='linux' or os.name=='posix':
        os.system("clear")

def pass_inp(message, name):
    
    return prompt(
        {
        'type': 'password',
        'message': message,
        'name': name
        }
    )

def yn_prompt(message, name):

    resp = prompt(
            {
                'type': 'confirm',
                'message': message,
                'name': name,
                'default': True,
            }
        )
    return resp

def get_who():
    who = [
            {
        'type': 'list',
        'name': 'who',
        'message': 'Teacher or Student',
        'choices': ['Teacher',Separator(),'Student'],
        'filter': lambda val: val.lower()
            }
        ]
    return prompt(who)['who']

def get_login_register():
    what = [
            {
        'type': 'list',
        'name': 'what',
        'message': 'Login/Register',
        'choices': ['Login',Separator(),'Register'],
        'filter': lambda val: val.lower()
            }
        ]
    return prompt(what)['what']


available_courses = [
    {
        'type': 'checkbox',
        'message': 'Select the courses for the enrollment',
        'name': 'courses',
        'choices': [ 
            Separator(),
            {
                'name': '19ELC311 - Computer Networks and Industrial Communication'
            },
            {
                'name': '19ELC312 - Database Systems and Programming'
            },
            {
                'name': '19ELC313 - Power Electronics and Drives'
            },
            {
                'name': '19ELC381 - Open Lab'
            },
            {
                'name': 'CIR_ELC_2022 - Soft Skills III'
            },
            {
                'name': '19LAW300 - Indian Constitution'
            },
            Separator()
        ]
    }
]

elective1 = [
        {   
        'type': 'list',
        'name': 'elective1',
        'message': 'Choose an elective',
        'choices': [
            '19CSE366 - Cyber Security',
            '19CSE448 - Block Chain',
            '21ECE431 - Neuroengineering'
            ]
        }
    ]

elective2 = [
        {   
        'type': 'list',
        'name': 'elective2',
        'message': 'Choose an elective',
        'choices': [
            '19EEE335 - Power Quality & FACTS',
            '19EEE434 - Automotive Electronics'
            ]
        }
    ]

teach_courses = [
        {'name':'19ELC311 - Computer Networks and Industrial Communication'},
        {'name':'19ELC312 - Database Systems and Programming'},
        {'name':'19ELC313 - Power Electronics and Drives'},
        {'name':'19ELC381 - Open Lab'},
        {'name':'CIR_ELC_2022 - Soft Skills III'},
        {'name':'19LAW300 - Indian Constitution'},
        {'name':'19CSE366 - Cyber Security'},
        {'name':'19CSE448 - Block Chain'},
        {'name':'21ECE431 - Neuroengineering'},
        {'name':'19EEE335 - Power Quality & FACTS'},
        {'name':'19EEE434 - Automotive Electronics'}
]

def register_courses():
    courses = {}

    c = prompt(available_courses)['courses']
    for i in c:
        splitted = i.split('-')
        courses[splitted[0]] = splitted[1]
    
    c = prompt(elective1)['elective1']
    courses[c.split('-')[0]] = c.split('-')[1]
    
    c = prompt(elective2)['elective2']
    courses[c.split('-')[0]] = c.split('-')[1]
    
    return courses

def teach_course():
    resp = prompt([{   
            'type': 'checkbox',
            'name': 'teach',
            'message': 'Choose the course to teach',
            'choices': teach_courses
            }])['teach']
    reg = {}
    for i in resp:
        splitted = i.split('-')
        reg[splitted[0]] = splitted[1]
    return reg
