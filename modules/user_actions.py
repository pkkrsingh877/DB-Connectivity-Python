from modules.attempt_quiz import attempt_quiz
from modules.result import result
from modules.show_profile import show_profile
from modules.update_profile import update_profile
from modules.show_leaderboard import show_leaderboard

def user_actions(is_logged_in, username_of_logged_in_user):
    print("-"*30)
    print("OPTIONS")
    print("-"*30)
    print('''
        1. Attempt Quiz
        2. View Result
        3. Show Profile
        4. Update Profile
        5. Show Leaderboard 
        6. Logout
    ''')
    print("-"*30)

    choice = input("What Operation do you want to perform: ")

    if choice == '1':
        attempt_quiz(is_logged_in, username_of_logged_in_user)
    elif choice == '2':
        result(is_logged_in, username_of_logged_in_user)
    elif choice == '3':
        print("View Profile Option selected")
        show_profile(is_logged_in, username_of_logged_in_user)
    elif choice == '4':
        update_profile(is_logged_in, username_of_logged_in_user)
    elif choice == '5':
        show_leaderboard()
    elif choice == '6':
        username_of_logged_in_user = ""
        is_logged_in = False
        print("-"*30)
        print("User Successfully Logged Out")
        print("-"*30)
        return True # Return to main function as user opted to logout
    else:
        print('Invalid Option!') # Corner Case : To be handled later
    print("-"*30)
    return False