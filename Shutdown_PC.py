import os
from Speak import Say
from Listen import Listen

def handle_shutdown():

    try:
        # Ask the user to confirm the shutdown using voice input
        Say("Are you sure you want to shut down the system? Please speak YES or NO.")
        response = Listen().lower()

        if "yes" in response:
            # Confirm the shutdown and provide feedback
            Say("Shutting down the system.")
            os.system("shutdown /s /t 1")
        elif "no" in response:
            # Provide feedback that shutdown was canceled
            Say("Shutdown canceled.")
    except:
        # Handle unrecognized responses
        Say("Sorry, I didn't understand your response. Shutdown canceled.")



