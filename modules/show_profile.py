import mysql.connector as database

from config import config

def show_profile(is_logged_in, username_of_logged_in_user):
    connection = database.connect(**config)
    cursor = connection.cursor()

    query = "SELECT * FROM user WHERE enrollment = %s;"
    cursor.execute(query, (username_of_logged_in_user,))

    row = cursor.fetchone() # Store previous query's data in row
    if row:
        name, enrollment, college, branch, contact = row[:5]
        print("*"*30)
        print("USER DETAILS")
        print("*"*30)
        print(f"Name: {name}\nEnrollment Number: {enrollment}\nCollege Name: {college}\nBranch Name: {branch}\nContact Number: {contact}")

    connection.close()