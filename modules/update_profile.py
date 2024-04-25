import mysql.connector as database

from config import config

def update_profile(is_logged_in, username_of_logged_in_user):
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
        print("*"*30)
        print("UPDATE USER DETAILS...")
        print("*"*30)
        print('''
            1. Name
            2. Username/Enrollment Number
            3. Password
            4. College Name
            5. Branch
            6. Contact Number
        ''')
        choice = input("What data do you want to update: ")
        updated_value = input("Enter updated data:")

        if choice == '1':
            query = "UPDATE user SET name = %s WHERE enrollment = %s;"
            data = (updated_value, username_of_logged_in_user,)
            cursor.execute(query,data)
            connection.commit()
        elif choice == '2':
            query = "UPDATE user SET enrollment = %s WHERE enrollment = %s;"
            data = (updated_value, username_of_logged_in_user,)
            cursor.execute(query,data)
            connection.commit()
        elif choice == '3':
            query = "UPDATE user SET password = %s WHERE enrollment = %s;"
            data = (updated_value, username_of_logged_in_user,)
            cursor.execute(query,data)
            connection.commit()
        elif choice == '4':
            query = "UPDATE user SET college = %s WHERE enrollment = %s;"
            data = (updated_value, username_of_logged_in_user,)
            cursor.execute(query,data)
            connection.commit()
        elif choice == '5':
            query = "UPDATE user SET branch = %s WHERE enrollment = %s;"
            data = (updated_value, username_of_logged_in_user,)
            cursor.execute(query,data)
            connection.commit()
        elif choice == '6':
            query = "UPDATE user SET contact = %s WHERE enrollment = %s;"
            data = (updated_value, username_of_logged_in_user,)
            cursor.execute(query,data)
            connection.commit()
        else:
            print("Invalid Choice!")
        print("*"*30)
        
    connection.close()