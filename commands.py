from enum import Enum
import psycopg2

class credentials_type(Enum) : 
    NAME = 0,
    EMAIL_ID = 1
    PASSWORD = 2
    COURSE_ID = 3
    COURSE_NAME = 4
    STUDENT_ID = 5
    TEACHER_ID = 6

def enum_to_query_string (type):
    match type:
        case credentials_type.NAME : 
            return 'name'
        case credentials_type.EMAIL_ID : 
            return 'email_id'
        case credentials_type.PASSWORD :
            return 'password'
        case credentials_type.COURSE_ID :
            return 'course_id'
        case credentials_type.COURSE_NAME :
            return 'course_name'
        case credentials_type.STUDENT_ID :
            return 'student_id'
        case credentials_type.TEACHER_ID : 
            return 'teacher_id'

def build_select_query(credentail_type : credentials_type,*arg : str) -> str:

    query = "select {0} from {1}".format(enum_to_query_string(credentail_type),arg[0])
    
    if len(arg) >= 2 : 
        conditional_query = " where"
        for i in range(1,len(arg)) : 
            conditional_query += " {}".format(arg[i])
            if i != len(arg) - 1 : 
                conditional_query += " and"
        query += conditional_query

    query += ';'

    return query

def response(request : str,db_conn) : 

    cur = db_conn.cursor()
    values = cur.execute(request)
    values = cur.fetchall()

    values = [i[0] for i in values]

    return values