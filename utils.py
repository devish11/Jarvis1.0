# utils.py: Utility functions for text processing, email formatting, and greeting

import datetime

def fix_email_spoken(text):
    """Convert spoken text to email/phone format by replacing common words with symbols.
    
    Converts spoken email addresses (e.g., "user at gmail dot com") to proper format (user@gmail.com).
    Also works for phone numbers and other text that needs symbol substitution.
    
    Args:
        text (str): Spoken text containing words like 'at', 'dot', 'dash'
    
    Returns:
        str: Formatted text with symbols substituted for words
    """
    replacements = {
        " at ": "@",          # 'at' becomes '@'
        " dot ": ".",        # 'dot' becomes '.'
        " underscore ": "_", # 'underscore' becomes '_'
        " dash ": "-",       # 'dash' becomes '-'
        " " : "",            # Remove spaces
        " space ": "",       # 'space' becomes empty
        " ": "",             # Final space cleanup
    }

    # Convert to lowercase for consistency
    text = text.lower()

    # Apply all replacement rules
    for word, symbol in replacements.items():
        text = text.replace(word, symbol)

    return text

# Prompt template for AI-generated email composition
prompt = """ You are an email-writer assistant. Your job is to produce the FINAL email exactly as it should be sent.
Do NOT include explanations, prompts, suggestions, instructions, bullet points, or commentary.
Do NOT tell the user what you are doing.
ONLY output the final ready-to-send email body."""

# System prompt that defines Jarvis personality and behavior for all AI responses
system_prompt = """
Your name is Jarvis.
 You are a polite, smart, fast voice assistant.
You always reply as Jarvis.
Keep responses short unless the user asks for details.
You are Created By Devish.
Don't Mention Jarvis While Replying. """

def greet_user():
    """Generate a context-aware greeting based on time of day.
    
    Returns:
        str: Appropriate greeting for current time of day
    """
    hour = datetime.datetime.now().hour

    # Morning: 5:00 AM - 11:59 AM
    if 5 <= hour < 12:
        return("Good Morning, Sir. How may I assist you?")
    # Afternoon: 12:00 PM - 4:59 PM
    elif 12 <= hour < 17:
        return("Good Afternoon, Sir. How may I assist you?")
    # Evening: 5:00 PM - 8:59 PM
    elif 17 <= hour < 21:
        return("Good Evening, Sir. How may I assist you?")
    # Night: 9:00 PM - 4:59 AM
    else:
        return("Hello Sir, it's quite late. How may I assist you?")