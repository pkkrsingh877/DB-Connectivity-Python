def register(connection, cursor):
    print("*"*30)
    print("REGISTER NEW USER...")
    print("*"*30)
    name = input("Enter Name: ")
    enrollment = input("Enter Enrollment Number: ")
    college = input("Enter College Name: ")
    branch = input("Enter Branch Name: ")
    contact = input("Enter Contact Number: ")
    password = input("Enter Password: ")

    print("*"*30)

    query = "INSERT INTO user (name, enrollment, college, branch, contact, password) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (name, enrollment, college, branch, contact, password)
    cursor.execute(query, data)
    connection.commit()
    print("Registration Complete...")