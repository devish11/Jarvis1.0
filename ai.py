"""AI integration helpers using Google's Gemini API.

This module provides a thin wrapper around the `genai` client to send a
prompt and return the text response. The `system_prompt` from `utils`
is prepended to guide the assistant's behavior.
"""

from google import genai
from config import API_KEY
from utils import system_prompt

# Initialize a reusable Gemini client with the provided API key
client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt: str) -> str:
    """Send a prompt to Gemini and return the assistant's reply as text.

    The `system_prompt` is prepended to every request so the assistant
    maintains consistent personality and instructions.

    Args:
        prompt: User input or instruction to send to Gemini.

    Returns:
        The text response from the model, or a friendly error message
        if the API call fails.
    """
    full_prompt = f"{system_prompt}\nUser: {prompt}"
    try:
        # Use a lightweight flash model for fast responses; swap model
        # name if you have access to other Gemini variants.
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_prompt,
        )
        return response.text
    except Exception as e:
        # Print error for debugging but return a user-friendly message
        print("Gemini API error:", e)
        return "Some Error Occurred. Sorry From Jarvis"


def start_assistant(query: str) -> str:
    """Public wrapper used by other modules to get an AI response."""
    return ask_gemini(query)
