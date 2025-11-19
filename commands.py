# commands.py: Implements core assistant commands (email, WhatsApp, system control, website opening)

import webbrowser
import os
import datetime 
import smtplib
import pywhatkit 
import voice as vc
import config as c

def open_website(q):
    """Open a predefined website in the default web browser.
    
    Args:
        q (str): URL of the website to open
    """
    try:
        webbrowser.open(q)
    except Exception as e:
        vc.speak("Sorry Sir, Could you please repeat that?")            

def time():
    """Return the current system time as a formatted string.
    
    Returns:
        str: Formatted time string (HH:MM:SS)
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
    
