import mysql.connector as database

from config import config

def result(is_logged_in, username_of_logged_in_user):
    connection = database.connect(**config)
    cursor = connection.cursor()

    query = "SELECT id FROM user WHERE enrollment = %s"
    user_data = (username_of_logged_in_user,)
    cursor.execute(query, user_data)
    row = cursor.fetchone()
    
    if row:
        query = "SELECT * FROM quiz_result WHERE student_id = %s;"
        user_id = (row[0],)
        cursor.execute(query, user_id)
        quiz_result = cursor.fetchall()

        if quiz_result:
            for result in quiz_result:
                print("-"*30)
                print("RECORD")
                print("-"*30)
                id, tag, correct, incorrect, percentage, total, student_id = result 
                print(f"id: {id}\nCategory:{tag}\nCorrect Questions: {correct}\nIncorrect Question: {incorrect}\nTotal Questions: {total}\nPercentage: {percentage}\nStudent Id: {student_id}")

    return False