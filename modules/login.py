def login(connection, cursor):
    username = input("Enter Username: ") #enrollment

    query = "SELECT * FROM student WHERE enrollment = %s"
    data = (username,)
    rows = cursor.execute(query,data)

    if rows:
        password = input("Enter Password: ") 

        query = "SELECT * FROM student WHERE password = %s"
        data = (password,)
        rows = cursor.execute(query,data)
        print(rows)
        print("*"*30)
        print("Login Successful")
        print("*"*30)