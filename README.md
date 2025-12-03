# Jarvis 1.0

Jarvis 1.0 is a modular, voice-driven automation system built using Python.  
It provides a structured framework for speech recognition, command execution, system automation, and database-based task handling.

The project is designed with a clean architecture that separates core components like:  
- Voice Input/Output  
- Command Processing  
- AI Logic  
- Database Interaction  
- Utility Functions  
- Configuration Management  

---

## Overview

Jarvis listens for voice input, interprets the intent, and executes the appropriate system or application command.  
The architecture allows for easy extensibility: add new skills, workflows, or integration with external APIs.

---

## Core Features

- Speech-to-Text & Text-to-Speech  
- Configurable command routing  
- System automation  
- Database logging & retrieval  
- Extendable AI logic  
- Modular, maintainable codebase  

---

## Project Structure

```
Jarvis1.0/
 ├── ai.py
 ├── commands.py
 ├── config.py
 ├── db.py
 ├── db_setup.py
 ├── main.py
 ├── utils.py
 ├── voice.py
 ├── working.py
 └── requirement.txt
```

---

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/devish11/Jarvis1.0.git  
   cd Jarvis1.0

2. Install dependencies:
   ```bash
   pip install -r requirement.txt  

3. (Optional) Initialize database:
    ```bash
    python db_setup.py  

4. Start the assistant:
    ```bash
    python main.py  

---

## Customization

1. Define new commands inside commands.py

2. Configure voice behavior, language, and speed in config.py

3. Extend AI logic in ai.py

4. Integrate APIs (Gemini, GPT, Weather, etc.)


---

## License

This project is licensed under the [MIT License](./LICENSE).

---
   
