# voice.py: Handles voice input (speech recognition) and voice output (text-to-speech)

import speech_recognition as sr
from gtts import gTTS
import os 
from playsound import playsound
import ai
from utils import greet_user


def take_command():
    """Listen to user voice input and convert speech to text using Google Speech Recognition.
    
    Returns:
        str: Recognized command text or error message
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        # Recognize speech using Google's speech recognition API (Indian English)
        command = r.recognize_google(audio, language='en-in')
        print("User said: " + command)
    except Exception as e:
        return "Some Error Ocuured. Sorry from Jarvis"
    return command

def speak(text):
    """Convert text to speech and play audio using Google Text-to-Speech.
    
    Args:
        text (str): Text to convert to speech
    """
    # Generate speech from text using gTTS (Google Text-to-Speech)
    tts = gTTS(text=text, lang='en', slow=False)
    fname = "voice.mp3"
    tts.save(fname)
    # Play the generated audio file
    playsound(fname)
    # Clean up temporary audio file
    os.remove(fname)

def start():
    """Continuously listen for wake word 'jarvis' and respond with greeting.
    
    This function runs in a loop waiting for voice activation with the wake word.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        while True:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                # Activate on 'jarvis' wake word
                if "jarvis" in text.lower():
                    speak(greet_user)
            except:
                pass