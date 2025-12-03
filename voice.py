"""Speech I/O helpers: listen for voice and play TTS audio.

This module uses the `speech_recognition` package for microphone input
and `gTTS` + `playsound` to synthesize and play audio.
"""

import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound


def take_command():
    """Listen to the microphone and return recognized text.

    Returns:
        The recognized string in lowercase, or the literal "none" when
        speech could not be understood or a timeout occurred.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        # Reduce sensitivity to ambient noise for better recognition
        recognizer.adjust_for_ambient_noise(source, duration=0.3)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
        except sr.WaitTimeoutError:
            return "none"

    try:
        command = recognizer.recognize_google(audio, language='en-in')
        print("User said:", command)
        return command.lower()

    except sr.UnknownValueError:
        # Speech was unintelligible
        return "none"

    except sr.RequestError as e:
        # API/network problems
        print("Speech Recognition API Error:", e)
        return "none"


def speak(text):
    """Convert `text` to speech using Google TTS and play it.

    The function saves a temporary `voice.mp3` file, plays it and removes
    the file. Exceptions are logged to stdout for debugging.
    """
    try:
        tts = gTTS(text=text, lang='en', slow=False)

        fname = "voice.mp3"
        tts.save(fname)

        playsound(fname)

        os.remove(fname)

    except Exception as e:
        print("Error in speak():", e)


def wake_word_listener(wake_word="jarvis"):
    """Block until the configured wake word is heard and return True.

    The function runs an infinite loop listening in short intervals and
    returns when the wake word is detected. It intentionally swallows
    transient recognition errors to keep the loop robust.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print(f"Listening for wake word: {wake_word}...")
        recognizer.adjust_for_ambient_noise(source)

    while True:
        with sr.Microphone() as source:
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                query = recognizer.recognize_google(audio, language='en-in').lower()
                print("Heard:", query)

                if wake_word.lower() in query:
                    print("Wake word detected!")
                    return True

            except sr.UnknownValueError:
                continue  # ignore noise

            except sr.WaitTimeoutError:
                continue

            except sr.RequestError:
                print("Speech Recognition API unavailable.")
                continue
