import mysql.connector as database
import os
from dotenv import load_dotenv
from config import config

# Top Level Functions/Modules
from modules.register import register
from modules.login import login

# Global variables
is_logged_in = False
username_of_logged_in_user = ""

def exitt():
    global connection, cursor
    connection.commit()
    cursor.close()
    connection.close()
    print("*"*30)
    print("Exiting The Program...")
    print("*"*30)
    exit()

def main():
    # Load environment variables from .env file
    load_dotenv()

    connection = database.connect(**config)

    print("*"*30)
    print('''
        1. Register
        2. Login
        3. Exit
    ''')
    print("*"*30)

    choice = input("What Operation do you want to perform: ")

    if choice == '1':
        register()
    elif choice == '2':
        login(is_logged_in, username_of_logged_in_user)
    elif choice == '3':
        exitt()
    else:
        print('Invalid Option!')

if __name__ == '__main__':
    main()