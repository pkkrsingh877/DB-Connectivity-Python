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
