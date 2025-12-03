"""Initialize the MySQL database and create required tables.

This script is intended to be run once when installing or setting up the
assistant. It creates the database (if missing) and a single table
`ai_log` that stores user commands, AI responses and timestamps.

Usage: run this script with a Python interpreter that has access to
the MySQL server configured in `config.py`.
"""

# Standard MySQL connector import (DB-API)
import mysql.connector as mysql
# Import DB credentials from project config
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

# Connect to MySQL server (not selecting a database yet)
mycon = mysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD
)

# Cursor used to execute SQL statements
cursor = mycon.cursor()

# Create the database if it does not already exist
cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME))
mycon.commit()
print("Database created successfully!")

# Switch the connection to use the newly created (or existing) database
cursor.execute("USE {}".format(DB_NAME))
mycon.commit()

# Create a simple table to store AI interaction logs
query2 = """CREATE TABLE IF NOT EXISTS ai_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    command VARCHAR(255) NOT NULL,
    response TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
"""
cursor.execute(query2)
mycon.commit()
print("Table 'ai_log' created successfully!")

# Close connection cleanly
mycon.close()