"""Centralized configuration for the Jarvis assistant.

Keep credentials, API keys, and simple site shortcuts here. This file is
imported by other modules (e.g. `db.py`, `ai.py`).

Note: Storing secrets in source files is convenient for local testing
but not recommended for production. Consider environment variables or
an encrypted secrets store for real deployments.
"""

# ==================== DATABASE CONFIGURATION ====================
# MySQL database connection credentials
DB_USER = "root"              # MySQL username
DB_PASSWORD = "1234"          # MySQL password
DB_HOST = "localhost"         # MySQL server host
DB_NAME = "jarvis_backup"     # Database name for storing chat logs

# ==================== API KEYS ====================
# Google Gemini API key for AI responses
API_KEY = ""
# NOTE: Keep API keys private. For personal projects this file is
# convenient, but in shared or production environments prefer
# environment variables or a secrets manager (e.g., Vault, AWS Secrets).

# ==================== EMAIL CONFIGURATION ====================
# Gmail account credentials for sending emails via SMTP
mail = ""        # Sender email address
password = ""            # Gmail App Password
# If using Gmail, generate an App Password for SMTP access and
# avoid storing your regular account password here.

# ==================== WEBSITE SHORTCUTS ====================
# Predefined websites that can be opened via voice commands
# Format: [command_name, url]
# `sites` maps a spoken keyword to a URL. The assistant uses the
# spoken key to look up and open the corresponding website. Add or
# remove entries as needed. Keep keys short and easy to say.
sites = {
	"youtube": "https://www.youtube.com",
	"wikipedia": "https://www.wikipedia.com",
	"google": "https://www.google.com",
	"github": "https://github.com",
}


