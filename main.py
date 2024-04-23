import mysql.connector as database
import os
from dotenv import load_dotenv
import string

# Top Level Functions/Modules
from modules.register import register
from modules.login import login

# Global variables
connection = None
cursor = None
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

def validate_password(password):
    # 1 uppercase, 1 lowercase, 1 digit, min length = 8, max length = 20
    # 1 special character
    isUppercase = False
    isLowercase = False
    minLength = False
    maxLength = False
    isDigit = False
    isSpecialCharacter = False
    
    if len(password) >= 8 and len(password) <= 20:
        minLength = True
        maxLength = True
        for letter in password:
            
            if letter in string.ascii_uppercase:
                isUppercase = True
            if letter in string.ascii_lowercase:
                isLowercase = True
            if letter in string.digits:
                isDigit = True
            if letter in string.punctuation:
                isSpecialCharacter = True
    
    if isUppercase and isLowercase and minLength and maxLength and isDigit and isSpecialCharacter:
        return True

def main():
    global connection, cursor
    # Load environment variables from .env file
    load_dotenv()

    connection = database.connect(
        host= os.getenv('HOST'),
        port= os.getenv('PORT'),
        user= os.getenv('USER'),
        password= os.getenv('PASSWORD'),
        database= os.getenv('DATABASE')
    )

    cursor = connection.cursor()

    print("*"*30)
    print('''
        1. Register
        2. Login
        3. Exit
    ''')
    print("*"*30)

    choice = input("What Operation do you want to perform: ")

    if choice == '1':
        register(connection, cursor)
    elif choice == '2':
        login(connection, cursor, is_logged_in, username_of_logged_in_user)
    elif choice == '3':
        exitt()
    else:
        print('Invalid Option!')

if __name__ == '__main__':
    main()

'''
TOP LEVEL FEATURE

1. REGISTER
2. LOGIN
3. ATTEMPT QUIZ
4. RESULT
5. EXIT

WITHIN LOGIN FEATURE

1. Attempt Quiz
2. View Result
3. Show Profile
4. Update Profile

WAP validate 
'''