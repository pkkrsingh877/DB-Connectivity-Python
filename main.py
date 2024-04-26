import mysql.connector as database
import os
from dotenv import load_dotenv
from config import config

# Top Level Functions/Modules
from modules.register import register
from modules.login import login
from modules.keep_going import keep_going
from modules.user_actions import user_actions

# Global variables
is_logged_in = False
username_of_logged_in_user = ""

def exitt():
    print("-"*30)
    print("Exiting The Program...")
    print("-"*30)
    exit()

def main():
    global is_logged_in, username_of_logged_in_user

    keep_running = True
    # Load environment variables from .env file
    load_dotenv()

    while keep_running:
        print("-"*30)
        print('''
            1. Register
            2. Login
            3. Exit
        ''')
        print("-"*30)

        choice = input("What Operation do you want to perform: ")

        if choice == '1':
            register()
        elif choice == '2':
            has_logged_out = login()
            while not has_logged_out:
                has_logged_out = user_actions()
        elif choice == '3':
            exitt()
        else:
            print('Invalid Option!')
        
        print("-"*30)
        print("Want to Continue Running Application")
        keep_running = keep_going()
        print("-"*30)



if __name__ == '__main__':
    main()