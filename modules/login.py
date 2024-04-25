import mysql.connector as database

from config import config
from modules.attempt_quiz import attempt_quiz
from modules.result import result
from modules.show_profile import show_profile
from modules.update_profile import update_profile

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
                print("*"*30)
                print("Login Successful")
                print("*"*30)

                print("*"*30)
                print("OPTIONS")
                print("*"*30)
                print('''
                    1. Attempt Quiz
                    2. View Result
                    3. Show Profile
                    4. Update Profile
                    5. Logout
                ''')
                print("*"*30)

                choice = input("What Operation do you want to perform: ")

                if choice == '1':
                    attempt_quiz(is_logged_in, username_of_logged_in_user)
                elif choice == '2':
                    result(is_logged_in, username_of_logged_in_user)
                elif choice == '3':
                    show_profile(is_logged_in, username_of_logged_in_user)
                elif choice == '4':
                    update_profile(is_logged_in, username_of_logged_in_user)
                elif choice == '5':
                    username_of_logged_in_user = ""
                    is_logged_in = False
                    print("*"*30)
                    print("User Successfully Logged Out")
                    print("*"*30)
                    return # Return to main function as user opted to logout
                else:
                    print('Invalid Option!')
                print("*"*30)
            else:
                print("Incorrect Password!")
    connection.close()