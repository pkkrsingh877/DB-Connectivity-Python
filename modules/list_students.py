def listStudents():
    global cursor
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