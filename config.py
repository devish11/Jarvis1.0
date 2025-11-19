# config.py: Centralized configuration file for Jarvis voice assistant
# Contains database credentials, API keys, email settings, and website shortcuts

# ==================== DATABASE CONFIGURATION ====================
# MySQL database connection credentials
DB_USER = "root"              # MySQL username
DB_PASSWORD = "1234"          # MySQL password
DB_HOST = "localhost"         # MySQL server host
DB_NAME = "jarvis_backup"     # Database name for storing chat logs

# ==================== API KEYS ====================
# Google Gemini API key for AI responses
API_KEY = "" 

# ==================== EMAIL CONFIGURATION ====================
# Gmail account credentials for sending emails via SMTP
mail = ""        # Sender email address
password = ""            # App password for gmail (not regular password)

# ==================== WEBSITE SHORTCUTS ====================
# Predefined websites that can be opened via voice commands
# Format: [command_name, url]
sites = [
    ["youtube", "https://www.youtube.com"],
    ["wikipedia", "https://www.wikipedia.com"],
    ["google", "https://www.google.com"],
    ["github", "https://www.github.com"],
]
