""" Connecting to databse using pgsql """ 

import sys
import psycopg2

class DB_Backend:
    
    conn = None

    def __init__(self,username,host,password):
        
        self.conn = self.DB_Login(username,host,password) 

    def DB_Login(self,username,host,password):
        
        conn = None
        try : 
            conn = psycopg2.connect(
                user = username,
                host = host,
                password = password
            )
        except psycopg2.OperationalError as error:
            print(error)
            sys.exit(0)
        else :
            print("Connected to server ! ")
            return conn

    def DB_Logout(self):

        self.conn.close()

