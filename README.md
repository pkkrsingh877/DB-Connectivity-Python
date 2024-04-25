# Quiz Application

This application is built using Python Language and MariaDB database. It is a console based application.

- Users can Register to create an account.
- Users who have registerd can Login to their account.
- Logged In Users can
    - Attempt Quiz
    - View Result
    - View Profile
    - Update Profile

It uses libraries like

    - mysql-connector-python : for connecting to MariaDB Database
    - dotenv-python : for creating enviornment variables to protect Database related information
    - os : for using dotenv-python
    - string : for string manipulation

Things that I can add to overall improve this application

    - I can use testing libraries to write test cases.
    - I also need to rewrite the functions so they are purely independent elements and are testable.
    - I can add some error handling especially if the errors are generated in Database operations.