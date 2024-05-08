import sqlite3

# Database connection setup
def connect_to_database():
    return sqlite3.connect('data/my_database.db')
