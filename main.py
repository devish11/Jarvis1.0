"""Main entrypoints for running the Jarvis assistant.

This module wires voice I/O, the AI backend and local command helpers
to produce the assistant's behavior. The `start_jarvis` function is the
runtime loop that listens for the wake word and dispatches commands to
`main` for handling.
"""

import ai
import commands as cmd
import db
import voice as vc
import config as cfg
import utils as uls
import os


def main(query):
    """Handle a single user query string and perform appropriate action.

    The function tries to match known command patterns (time, shutdown,
    email, messages, etc.). If none match, the query is forwarded to the
    AI assistant. The returned/produced string is also logged to the DB.

    Args:
        query: Text of the user's command (lowercased by caller).
    """
    # --------------------------
    # TIME
    # --------------------------
    # Return current system time
    if "time" in query and "right now" in query:
        b = cmd.tell_time()
        vc.speak(b)

    # --------------------------
    # SHUTDOWN
    # --------------------------
    # Shut down the system
    elif "shutdown" in query:
        vc.speak("Shutting down the system")
        b = cmd.shutdown()
        a = False  # Exit main loop

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

            b = "Sending message to"+ to + ":" + msg
            cmd.send_whatsapp(number, msg)

        except Exception:
            b = "Sorry Sir. I am unable to send the message right now."
            vc.speak(b)
    
    elif "open" in query or "search" in query:
        # Normalize the command by removing wake-word and the verb
        query = query.replace("jarvis", "").replace("open", "").strip()

        # NOTE: `cfg.sites` in `config.py` is a list of [name,url] pairs.
        # The original code checks `cfg.sites.keys()` which will raise
        # AttributeError if `sites` is not a dict. Here we keep behavior
        # unchanged but add a helpful comment for future maintainers.
        if query in cfg.sites.keys():
            # If the site key is known, delegate to `cmd.web` (assumed to
            # open a site by key). Speak confirmation to the user.
            cmd.web(query)
            vc.speak("Opening Sir")
        else:
            # If no predefined site matches, do a general search instead.
            vc.speak("Ok sir")
            cmd.search(query)


    elif "play" in query:
        # Extract the song/playlist identifier from the spoken command
        query = query.replace("jarvis", "").replace("play", "").strip()

        # Inform the user and hand off to the player helper. The
        # `cmd.play_song` implementation is expected to accept an
        # optional query string identifying what to play.
        vc.speak("Playing sir")
        cmd.play_song(query)


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
    # DEFAULT → AI RESPONSE
    # --------------------------
    # If no specific command matches, use AI to generate response
    else:

        b = ai.start_assistant(query)
        print("Jarvis:", b)
        vc.speak(b)

    # Save interaction to database
    try:
        # Persist the user's query and the assistant's response. This
        # uses a short-lived DB connection inside `db.response` so errors
        # are isolated from the main loop.
        db.response(query, b)
    except:
        pass

def start_jarvis():
    """Start the assistant's wake-word loop and process incoming queries.

    This function blocks: it listens for the configured wake word
    (default "jarvis") and then repeatedly calls `main` for each
    detected command phrase. Saying a stop/close command will exit the
    loop and end the program.
    """
    vc.wake_word_listener("jarvis")
    vc.speak("sir..")
    a = True
    while a:
        query = vc.take_command().lower()
        if "jarvis" in query:
            multiquery = query.split("and")
            for i in multiquery:
                if "stop" in i or "close" in i and "jarvis" in i:
                    vc.speak("Goodbye sir.")
                    a = False
                else:
                    main(i)


if __name__ == "__main__":
    start_jarvis()