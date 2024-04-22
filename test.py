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
    print("*"*30)
    print("REGISTER NEW STUDENT")
    print("*"*30)
    name = input("Enter Name: ")
    enrollment = input("Enter Enrollment Number: ")
    college = input("Enter College Name: ")
    branch = input("Enter Branch Name: ")
    contact = input("Enter Contact Number: ")
    print("*"*30)

    query = "INSERT INTO student (name, enrollment, college, branch, contact) VALUES (%s, %s, %s, %s, %s)"
    data = (name, enrollment, college, branch, contact)
    cursor.execute(query, data)
    print("Registration Complete...")
    exitt()

def login():
    pass

def listStudents():
    query = "SELECT name, enrollment FROM student;"

    cursor.execute(query)

    rows = cursor.fetchall() # Store previous query's data in rows

    print("*"*30)
    print("Name\t\t\t\tEnrollement")
    print("*"*30)
    for row in rows:
        name, enrollment = row # Destructuring
        print(f"{name}\t\t\t{enrollment}")
    print("*"*30)
    exitt()

def listStudent():
    enrollment = input('Enter Enrollment Number: ')
    query = "SELECT * FROM student WHERE enrollment = %s;"
    
    cursor.execute(query, (enrollment,))

    row = cursor.fetchone() # Store previous query's data in row
    if row:
        name, enrollment, college, branch, contact = row[:5]
        print("*"*30)
        print("STUDENT DETAILS")
        print("*"*30)
        print(f"Name: {name}\nEnrollment Number: {enrollment}\nCollege Name: {college}\nBranch Name: {branch}\nContact Number: {contact}")
    else:
        print("Student with entered Enrollment Number does not exist...")
    
    exitt()

def exitt():
    connection.commit()
    cursor.close()
    connection.close()
    print("*"*30)
    print("Exitting The Program...")
    print("*"*30)
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
