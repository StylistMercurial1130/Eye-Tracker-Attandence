""" Connecting to databse using pgsql """ 

import sys
import psycopg2

"""
    request :
        -> Database : "<insert-data-base-name>" eg : lets say database hospital 
        -> operation : "<insert-operation-here"> eg : SELECT
        -> requested_data : [somedata_1,somedata_2,...]
        -> Send_Error : bool(true/false) only for debug

    response  :
        -> request_data : [whaterver_data_you_wanded_1,.....]
        -> Error : <some-error-because-you-messed-up-somewhere>
    
"""

class DB_Backend:
    
    conn = None

    def __init__(self,username,host,password,dbname):
        
        self.conn = self.DB_Login(username,host,password,dbname) 

    def DB_Login(self,username,host,password,dbname):
        
        conn = None
        try : 
            conn = psycopg2.connect(
                user = username,
                host = host,
                password = password,
                dbname = dbname
            )
        except psycopg2.OperationalError as error:
            """
                Oh boiiii, you screwed up didnt you !. God bless your soul if your dont realize it    
            """
            print(error)
            sys.exit(0)
        else :
            """
                Congratulation ! 
                Celebrations ! 
                you connected to server !
                you have achiever absolutely nothing, incosequnetial to the grander scheme of things known as life
                I genuniely feel sorry for you
            """

            print("Connected to server ! ")
            return conn

    
    def DB_Serve(request):

        """collect data from request"""
        operation = request["operation"]
        requested_data = request["requested_data"]
        send_error = request["send_error"]

        


    def DB_Logout(self):

        self.conn.close()




