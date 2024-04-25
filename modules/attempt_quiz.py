from modules.result import result

def attempt_quiz(connection, cursor, is_logged_in, username_of_logged_in_user):
    percentage = 0
    total = 0
    correct = 0 
    incorrect = 0 
    student_id = 1
    tag = ""
    query = "SELECT * FROM quiz_question WHERE tag = 'HTML' ORDER BY RAND() LIMIT 5"
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)

    for row in rows:
        id, question, option1, option2, option3, option4, correct_option, tag = row[:8]
        print("*"*30)
        print("Question")
        print("*"*30)
        print(question)
        print(f"1. {option1}")
        print(f"2. {option2}")
        print(f"3. {option3}")
        print(f"4. {option4}")
        choice = input("Answer: ")
        total += 1
        if choice == correct_option:
            correct += 1
        else:
            incorrect += 1
    
    percentage = correct*20

    query = "SELECT * FROM user WHERE enrollment = %s"
    data = (username_of_logged_in_user,)
    cursor.execute(query, data)
    row = cursor.fetchone()
    print(row)

    if row:
        student_id = row[5]

    query = "INSERT INTO quiz_result(tag, correct, incorrect, percentage, total, student_id) VALUES (%s, %s, %s, %s, %s, %s);"
    data = (tag, correct, incorrect, percentage, total, student_id,)
    cursor.execute(query, data)
    connection.commit()

    result(connection, cursor, is_logged_in, username_of_logged_in_user)

