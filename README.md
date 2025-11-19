Jarvis 1.0 – Python Voice Assistant

Jarvis 1.0 is a modular voice-controlled personal assistant built using Python.
It supports speech recognition, automated system tasks, command handling, database logging, and customizable AI-based responses.
Designed for beginners and developers who want to understand how real voice assistants work under the hood.

🚀 Features

🎙 Voice Input using SpeechRecognition

🔊 Text-to-Speech Output

🧠 Command Execution Engine (open websites, system tasks, queries etc.)

🗄️ Database Integration (SQLite/MySQL based on your setup)

⚙️ Configurable Modules for easy customization

🧩 Modular Architecture — add new skills easily

🔌 API-ready structure for adding Gemini/GPT/Weather etc.

📁 Project Structure
Jarvis1.0/
│── ai.py              # AI logic & query handling
│── commands.py        # All supported commands
│── config.py          # App configuration settings
│── db.py              # Database operations
│── db_setup.py        # Database initialization
│── main.py            # Main entry point
│── utils.py           # Helper functions
│── voice.py           # Speech input/output
│── working.py         # Additional workflows
└── requirement.txt    # Project dependencies

🔧 Installation
Clone the Repository
git clone https://github.com/devish11/Jarvis1.0.git
cd Jarvis1.0

Install Dependencies
pip install -r requirement.txt

(Optional) Initialize Database
python db_setup.py

▶️ How to Run
python main.py


Jarvis will start listening for your commands such as:

“Open YouTube”

“What’s the time?”

“Search for programming tutorials”

“Play music”

⚙️ Customization
Add New Commands

Open commands.py

Create a new function (example):

def greet():
    vc.speak("Hello! How can I assist you today?")


Add it to your command mapping.

Modify Voice & Settings

Edit config.py for:

Voice type

Language

Speed

Activation behavior

Improve AI Logic

Enhance ai.py with NLP or external APIs like Gemini or GPT.

🤝 Contributing

Contributions, ideas, and pull requests are welcome.
You can help by:

Adding more commands

Improving accuracy

Integrating APIs

Fixing bugs

Enhancing documentation

📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it.
