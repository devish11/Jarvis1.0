# working.py: Main execution loop for Jarvis voice assistant
# Coordinates between voice I/O, AI responses, and command execution

import ai
import commands as cmd
import db
import voice as vc
import config as cfg
import utils as uls
import os


def main():
    """Main loop for Jarvis assistant.
    
    This function continuously listens for voice commands and processes them by:
    1. Listening for the wake word via start()
    2. Capturing user command
    3. Parsing command and executing appropriate action
    4. Logging interactions to database
    """
    a = True  # Outer loop control (while True)
    print("Initializing Jarvis 1.0")

    while a:
        # Listen for wake word 'jarvis'
        vc.start()
        # Get user command after wake word detected
        query = vc.take_command().lower()

        d = True  # Inner loop control (process one command)
        while d:

            # --------------------------
            # SITE OPENING LOGIC
            # --------------------------
            # Check if user wants to open a website
            for site in cfg.sites:
                if "open"+site[0].lower() in query:
                    vc.speak("Opening " + site[0] + " sir...")
                    cmd.open_website(site[1])
                    b = "Opening " + site[0] + " sir"
                    break

            # --------------------------
            # TIME
            # --------------------------
            # Return current system time
            if "time" in query and "right now" in query:
                b = cmd.time()
                vc.speak(b)

            # --------------------------
            # SHUTDOWN
            # --------------------------
            # Shut down the system
            elif "shutdown" in query:
                vc.speak("Shutting down the system")
                b = cmd.shutdown()
                a = False  # Exit main loop
                d = False  # Exit command loop

            # --------------------------
            # RESTART
            # --------------------------
            # Restart the system
            elif "restart" in query:
                vc.speak("Restarting the system")
                b = cmd.restart()

            # --------------------------
            # EMAIL
            # --------------------------
            # Send email through Gmail SMTP
            elif "email" in query:
                try:
                    # Get recipient email
                    vc.speak("Whom should I send it to?")
                    t1 = vc.take_command().lower()
                    to = uls.fix_email_spoken(t1)

                    # Get email subject
                    vc.speak("What is the subject?")
                    subject = vc.take_command()

                    # Ask if AI should generate content
                    vc.speak("Should I generate the content using AI?")
                    response = vc.take_command().lower()

                    if "yes" in response:
                        # Generate professional email using AI
                        content = ai.start_assistant("Generate a professional email about " + subject)
                        vc.speak(content)

                        # Ask for revisions
                        vc.speak("Do you want to make any changes?")
                        resp = vc.take_command().lower()

                        if "yes" in resp:
                            # Incorporate user changes via AI
                            vc.speak("What changes do you want to make?")
                            changes = vc.take_command()
                            content = content + ". Also include: " + changes
                            content = ai.start_assistant(
                                "Generate a professional email about "
                                + subject
                                + " with the following details: "
                                + content
                            )
                    else:
                        # Manually compose email
                        while True:
                            vc.speak("Tell me the content.")
                            content = vc.take_command()

                            vc.speak("Here is the content: " + content)
                            vc.speak("Is this correct?")

                            if "yes" in vc.take_command().lower():
                                break

                    b = f"Sending Email to {to} | Subject: {subject} | Content: {content}"
                    vc.speak("Sending Email...")
                    vc.speak(cmd.send_email(to, subject, content))

                except Exception:
                    b = "Sorry Sir. I am unable to send the email right now."
                    vc.speak(b)

            # --------------------------
            # WHATSAPP MESSAGE
            # --------------------------
            # Send WhatsApp message
            elif "message" in query:
                try:
                    # Get recipient phone number
                    vc.speak("Whom should I send it to?")
                    to = vc.take_command()

                    # Get message content
                    vc.speak("What do you want to send?")
                    msg = vc.take_command()

                    vc.speak("Sending message...")
                    # Convert spoken number format to digits
                    number = uls.fix_email_spoken(to)

                    b = f"Sending message to {to}: {msg}"
                    cmd.send_whatsapp(number, msg)

                except Exception:
                    b = "Sorry Sir. I am unable to send the message right now."
                    vc.speak(b)

            # --------------------------
            # CHAT LOG
            # --------------------------
            # Export chat history to CSV file
            elif "chat log" in query:
                try:
                    import csv
                    # Fetch all logs from database
                    logs = db.fetch_logs()

                    # Write logs to CSV file
                    with open("log.csv", "w", newline="") as f:
                        writer = csv.writer(f)
                        for log in logs:
                            writer.writerow(list(log))

                    # Open CSV file in default application
                    os.startfile("log.csv")
                    b = "Chat log exported."

                except Exception:
                    b = "Unable to fetch chat log."
                    vc.speak(b)

            # --------------------------
            # SLEEP MODE
            # --------------------------
            # Put assistant in standby mode
            elif "sleep" in query:
                vc.speak("I am on standby, sir.")
                d = False  # Exit command loop, return to listening

            # --------------------------
            # STOP / CLOSE
            # --------------------------
            # Close the application
            elif "stop" in query or "close jarvis" in query:
                vc.speak("Goodbye sir.")
                d = False  # Exit command loop
                a = False  # Exit main loop

            # --------------------------
            # DEFAULT → AI RESPONSE
            # --------------------------
            # If no specific command matches, use AI to generate response
            else:
                b = ai.start_assistant(query)
                print("Jarvis:", b)
                vc.speak(b)

            # Save interaction to database
            try:
                db.response(query, b)
            except:
                pass
