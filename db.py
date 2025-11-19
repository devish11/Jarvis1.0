
# db.py: Handles database operations for logging AI interactions and retrieving chat history

import mysql.connector as mysql  # mysql.connector implements the MySQL DB-API; aliased to `mysql` for brevity
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME  # DB credentials and connection settings from config.py

def response(command, answer):
    """Log user command and AI response to the database.
    
    Args:
        command (str): User command/query
        answer (str): AI's response
    """
    # Establish database connection
    mycon = mysql.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME
    )
    cursor = mycon.cursor()

    # Insert command and response with auto-timestamp
    query = "INSERT INTO ai_log (command, response) VALUES (%s, %s)"
    cursor.execute(query, (command, answer))
    mycon.commit()
    mycon.close()

def fetch_logs():
    """Retrieve all chat logs from database, sorted by most recent first.
    
    Returns:
        list: List of tuples containing (id, command, response, timestamp)
    """
    # Establish database connection
    mycon = mysql.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME
    )
    cursor = mycon.cursor()

    # Fetch all logs in reverse chronological order
    query = "SELECT * FROM ai_log ORDER BY timestamp DESC"
    cursor.execute(query)
    logs = cursor.fetchall()
    mycon.close()
    return logs