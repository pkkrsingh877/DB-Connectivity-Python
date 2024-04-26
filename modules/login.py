import mysql.connector as database

from config import config
from modules.attempt_quiz import attempt_quiz
from modules.result import result
from modules.show_profile import show_profile
from modules.update_profile import update_profile
from modules.user_actions import user_actions

def login(is_logged_in, username_of_logged_in_user):
    
    connection = database.connect(**config)
    cursor = connection.cursor()

    username = input("Enter Username: ") #enrollment

    query = "SELECT * FROM user WHERE enrollment = %s;"
    data = (username,)
    cursor.execute(query,data)
    rows = cursor.fetchall()

    if rows:
        while not is_logged_in:
            password = input("Enter Password: ") 

            query = "SELECT * FROM user WHERE enrollment = %s AND password = %s"
            data = (username, password,)
            cursor.execute(query,data)
            password_rows = cursor.fetchall()
            if password_rows:
                username_of_logged_in_user = username
                is_logged_in = True
                # User is logged in
                print("-"*30)
                print("Login Successful")
                print("-"*30)

                return user_actions(is_logged_in, username_of_logged_in_user)
