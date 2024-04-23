def listStudent():
    global cursor
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
        