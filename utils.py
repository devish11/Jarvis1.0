"""Utility helpers for text normalization and AI prompt templates.

Functions in this module help convert spoken fragments (e.g. "at",
"dot") into formatted email addresses or phone numbers. It also
contains templates used when calling the AI assistant to compose
emails or control assistant personality.
"""


def fix_email_spoken(text):
    """Convert spoken text to email/phone format by replacing common words.

    Example: "user at gmail dot com" -> "user@gmail.com"

    Args:
        text: Spoken representation of an email or number.

    Returns:
        A cleaned, symbol-substituted string.
    """
    # Replacement rules map common spoken tokens to their symbol equivalents.
    # Note: the mapping contains a general whitespace removal rule, so keep
    # token ordering careful if you change or extend the dictionary.
    replacements = {
        " at ": "@",          # 'at' becomes '@'
        " dot ": ".",        # 'dot' becomes '.'
        " underscore ": "_", # 'underscore' becomes '_'
        " dash ": "-",       # 'dash' becomes '-'
        " " : "",            # Remove spaces
        " space ": "",       # 'space' becomes empty
        " ": "",             # Final space cleanup
    }

    text = text.lower()

    for word, symbol in replacements.items():
        text = text.replace(word, symbol)

    return text


# Prompt template for AI-generated email composition. This template asks
# the model to produce a final-ready email body with no extra commentary.
prompt = """ You are an email-writer assistant. Your job is to produce the FINAL email exactly as it should be sent.
Do NOT include explanations, prompts, suggestions, instructions, bullet points, or commentary.
Do NOT tell the user what you are doing.
ONLY output the final ready-to-send email body."""


# System prompt that defines Jarvis personality and behavior for all AI responses
system_prompt = """
Your name is Jarvis.
You are a polite, smart, fast voice assistant.
Your build On Purely Python, with mysql as database.
You always reply as Jarvis.
Keep responses short unless the user asks for details.
You are Created By Devish.
Don't Say Created By Devish Everytime Without Asking.
Don't Mention Jarvis While Replying.
Don't Use Bold,Italic And * .
Don't Have Give Your API Key Or Your Codes.."""

