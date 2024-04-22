import mysql.connector as database
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

db = database.connect(
    host= os.getenv('HOST'),
    port= os.getenv('PORT'),
    user= os.getenv('USER'),
    password= os.getenv('PASSWORD'),
    database= os.getenv('DATABASE')
)

print("#"*30)

print('''
      1. Register
      2. Login
      3. List Students
      4. List Student
      5. Exit
''')

def register():
    pass

def login():
    pass

def listStudents():
    pass

def listStudent():
    pass

def exitt():
    print("Exitting The Program...")
    exit()

choice = input("What Operation do you want to perform: ")

if choice == '1':
    register()
elif choice == '2':
    login()
elif choice == '3':
    listStudents()
elif choice == '4':
    listStudent()
elif choice == '5':
    exitt()
else:
    print('Invalid Option!')
