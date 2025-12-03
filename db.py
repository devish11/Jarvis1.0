
"""Database helpers for logging and retrieving AI interaction history.

This module provides minimal functions used by `main.py` to persist
and fetch chat logs stored in the `ai_log` table.
"""

import mysql.connector as mysql  # mysql.connector implements the MySQL DB-API
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME


def response(command, answer):
    """Append a single command/response pair to the `ai_log` table.

    Args:
        command: The user's spoken/written command text.
        answer: The AI assistant's response text.
    """
    # Create a short-lived DB connection for this write operation
    mycon = mysql.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME,
    )
    cursor = mycon.cursor()

    # Parameterized query prevents injection and handles escaping
    query = "INSERT INTO ai_log (command, response) VALUES (%s, %s)"
    cursor.execute(query, (command, answer))
    mycon.commit()
    mycon.close()


def fetch_logs():
    """Return all chat logs ordered newest-first.

    Returns:
        A list of rows from `ai_log` as tuples: (id, command, response, timestamp).
    """
    mycon = mysql.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME,
    )
    cursor = mycon.cursor()

    query = "SELECT * FROM ai_log ORDER BY timestamp DESC"
    cursor.execute(query)
    logs = cursor.fetchall()
    mycon.close()
    return logs