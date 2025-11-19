"""db_setup.py: Initializes MySQL database and creates tables for logging AI interactions.

This script should be run once to set up the database structure. It creates:
- jarvis_backup database
- ai_log table for storing command/response history with timestamps
"""

# Import MySQL connector library
import mysql.connector as mysql
# Import database configuration credentials from config file
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

# Establish connection to MySQL server using credentials
mycon = mysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD
)

# Create cursor object to execute SQL queries
cursor = mycon.cursor()

# Create database if it doesn't already exist
cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME))
mycon.commit()
print("Database created successfully!")

# Select the newly created database for use
cursor.execute("USE {}".format(DB_NAME))
mycon.commit()

# Create ai_log table to store user interactions with AI system
query2 = """CREATE TABLE IF NOT EXISTS ai_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    command VARCHAR(255) NOT NULL,
    response TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)"""
cursor.execute(query2)
mycon.commit()
print("Table 'ai_log' created successfully!")

# Close database connection
mycon.close()