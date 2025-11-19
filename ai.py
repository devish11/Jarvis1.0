# ai.py: Handles AI integration with Google's Gemini API for intelligent responses

import google.generativeai as genai
from config import API_KEY
from utils import system_prompt

# Configure Gemini API with API key from config
genai.configure(api_key=API_KEY)

# Initialize Gemini 2.0 Flash model for fast, efficient responses
model = genai.GenerativeModel("gemini-2.0-flash")

def ask_gemini(prompt):
    """Send a prompt to Gemini AI and get a response.
    
    Args:
        prompt (str): User query or request
    
    Returns:
        str: AI-generated response or error message
    """
    # Combine system prompt with user prompt for context
    full_prompt = system_prompt + "\nUser:" + prompt
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return "Some Error Occured. Sorry From Jarvis"

def start_assistant(query):
    """Wrapper function to start the AI assistant.
    
    Args:
        query (str): User question or command
    
    Returns:
        str: Assistant's response
    """
    reply = ask_gemini(query)
    return reply