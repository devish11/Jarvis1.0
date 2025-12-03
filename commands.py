"""High-level system and messaging commands used by the assistant.

This module contains functions for system actions (shutdown/restart),
messaging (email, WhatsApp), simple PC search automation, and media
playback helpers. Functions are designed to be called from `main.py`.
"""

import os
import datetime
import smtplib
import pywhatkit
import keyboard
import config as c
import webbrowser
import time


def tell_time():
    """Return the current system time as a formatted string.

    Returns:
        A human readable time string in HH:MM:SS format.
    """
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return "The current time is " + now

def shutdown():
    """Shut down the system immediately (1 second delay)."""
    os.system("shutdown /s /t 1")

def restart():
    """Restart the system immediately (1 second delay)."""
    os.system("shutdown /r /t 1")

def send_email(to_email, subject, msg):
    """Send an email via Gmail SMTP server.
    
    Args:
        to_email (str): Recipient email address
        subject (str): Email subject line
        msg (str): Email body/message content
    
    Returns:
        str: Confirmation message
    """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    sender_email = c.mail
    password = c.password   

    server.login(sender_email, password)
    email_text = "Subject:"+subject+"\n\n"+msg

    server.sendmail(sender_email, to_email, email_text)
    server.quit()
    return "Email sent successfully"

def send_whatsapp(number, message):
    """Send a WhatsApp message using pywhatkit (schedules for next minute).
    
    Args:
        number (str): Recipient phone number (without country code, will add +91)
        message (str): Message content to send
    
    Returns:
        str: Confirmation message
    """
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 1  # Schedule for next minute

    pywhatkit.sendwhatmsg("+91"+number, message, hour, minute)
    return "WhatsApp message sent successfully"
    


def search(query):

    """Search inside Windows using WIN key + typing."""
    
    # Clean command
    query = query.replace("search", "").replace("open", "").replace("jarvis", "").strip()

    # Open Start Menu
    keyboard.press_and_release('windows')
    time.sleep(0.3)

    # Type what you want to search
    keyboard.write(query)
    time.sleep(0.4)

    # Open first result
    keyboard.press_and_release('enter')


def play_song(query):
    pywhatkit.playonyt(query)

def web(query):
    for site in c.sites:
            if site.lower() in query.lower():

                webbrowser.get("windows-default").open(c.sites[site])

