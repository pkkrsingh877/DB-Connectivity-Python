import mysql.connector as database
import os
from dotenv import load_dotenv

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

print("#"*30)

print('''
      1. Register
      2. Login
      3. List Students
      4. List Student
      5. Exit
''')

def register():
    name = input("Enter Name: ")
    enrollment = input("Enter Enrollment Number: ")
    college = input("Enter College Name: ")
    branch = input("Enter Branch Name: ")
    contact = input("Enter Contact Number: ")

    query = "INSERT INTO student (name, enrollment, college, branch, contact) VALUES (%s, %s, %s, %s, %s)"
    data = (name, enrollment, college, branch, contact)
    cursor.execute(query, data)
    print("Registration Complete...")

    connection.commit()
    cursor.close()
    connection.close()



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
