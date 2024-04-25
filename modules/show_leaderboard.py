import mysql.connector as database

from config import config

def show_leaderboard():
    connection = database.connect(**config)
    cursor = connection.cursor()

    connection.close()
    pass