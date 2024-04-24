def update_profile(connection, cursor, is_logged_in, username_of_logged_in_user):
    query = "SELECT * FROM student WHERE enrollment = %s;"
    cursor.execute(query, (username_of_logged_in_user,))

    row = cursor.fetchone() # Store previous query's data in row
    if row:
        name, enrollment, college, branch, contact = row[:5]
        print("*"*30)
        print("STUDENT DETAILS")
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
            query = "UPDATE student SET name = %s WHERE enrollment = %s;"
            data = (updated_value, username_of_logged_in_user,)
            cursor.execute(query,data)
            connection.commit()
        elif choice == '2':
            query = "UPDATE student SET enrollment = %s WHERE enrollment = %s;"
            data = (updated_value, username_of_logged_in_user,)
            cursor.execute(query,data)
            connection.commit()
        elif choice == '3':
            query = "UPDATE student SET password = %s WHERE enrollment = %s;"
            data = (updated_value, username_of_logged_in_user,)
            cursor.execute(query,data)
            connection.commit()
        elif choice == '4':
            query = "UPDATE student SET college = %s WHERE enrollment = %s;"
            data = (updated_value, username_of_logged_in_user,)
            cursor.execute(query,data)
            connection.commit()
        elif choice == '5':
            query = "UPDATE student SET branch = %s WHERE enrollment = %s;"
            data = (updated_value, username_of_logged_in_user,)
            cursor.execute(query,data)
            connection.commit()
        elif choice == '6':
            query = "UPDATE student SET contact = %s WHERE enrollment = %s;"
            data = (updated_value, username_of_logged_in_user,)
            cursor.execute(query,data)
            connection.commit()
        else:
            print("Invalid Choice!")
        print("*"*30)
        