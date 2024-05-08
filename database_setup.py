import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('data/my_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define the SQL command to create a table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
'''

# Execute the SQL command to create the table
cursor.execute(create_table_query)

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
