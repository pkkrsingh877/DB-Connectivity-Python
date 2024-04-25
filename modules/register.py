import mysql.connector as database

from config import config
from modules.validate_password import validate_password

def register():
    connection = database.connect(**config)
    cursor = connection.cursor()
    
    valid_password = False
    print("*"*30)
    print("REGISTER NEW USER...")
    print("*"*30)
    name = input("Enter Name: ")
    enrollment = input("Enter Enrollment Number: ")
    college = input("Enter College Name: ")
    branch = input("Enter Branch Name: ")
    contact = input("Enter Contact Number: ")
    while not valid_password:
        password = input("Enter Password: ")
        if validate_password(password):
            break
        print("Password should have atleast 1 uppercase, 1 lowercase, 1 special character, min length of 8 and max length of 20!")



    print("*"*30)

    query = "INSERT INTO user (name, enrollment, college, branch, contact, password) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (name, enrollment, college, branch, contact, password)
    cursor.execute(query, data)
    connection.commit()
    print("Registration Complete...")