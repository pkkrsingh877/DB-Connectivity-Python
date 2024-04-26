import mysql.connector as database

from config import config

def show_leaderboard():
    connection = database.connect(**config)
    cursor = connection.cursor()

    query = "SELECT user.name AS NAME, user.enrollment AS ENROLLMENT_NUMBER, correct AS CORRECT_ANSWERS, incorrect AS INCORRECT_ANSWERS, total AS TOTAL_ANSWERS, percentage AS PERCENTAGE from quiz_result INNER JOIN user ON quiz_result.student_id = user.id;"
    cursor.execute(query)
    rows = cursor.fetchall()

    print(f"Name\tEnrollement Number\tCorrect Answers\tIncorrect Answers\tTotal Answers\tPercentage")
    for row in rows:
        NAME, ENROLLMENT_NUMBER, CORRECT_ANSWERS, INCORRECT_ANSWERS, TOTAL_ANSWERS, PERCENTAGE = row
        print(f"{NAME}\t\t{ENROLLMENT_NUMBER}\t\t{CORRECT_ANSWERS}\t\t{INCORRECT_ANSWERS}\t\t{TOTAL_ANSWERS}\t\t{PERCENTAGE}")
        print('-'*30)   
    return False