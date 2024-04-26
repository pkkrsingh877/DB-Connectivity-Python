def keep_going():
    user_input = input("Yes/No: ").lower()

    if user_input == 'yes':
        return True
    elif user_input == 'no':
        return False
    else:
        print("Invalid Input!")
        keep_going()