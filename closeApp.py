import os
from Speak import Say
import pyautogui

# Define a dictionary of applications and their process names
# This dictionary maps friendly names to the process names used to close the application
app_process_names = {
    "paint": "mspaint.exe",
    "commandprompt": "cmd.exe",
    "word": "WINWORD.EXE",
    "excel": "EXCEL.EXE",
    "chrome": "chrome.exe",
    "vscode": "Code.exe",
    "powerpoint": "POWERPNT.EXE",
    "paint": "mspaint",
    "commandprompt": "cmd",
    "word": "winword",
    "excel": "excel",
    "chrome": "C:Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "powerpoint": "powerpnt",
    "Notepad": "notepad",
    "Calculator": "calc",
    "powerpoint": "powerpoint",
    "File Explorer": "explorer",
    "Microsoft Edge": "msedge",
    "Google Chrome": "chrome",
    "VLC Media Player": "vlc",
    "Spotify": "spotify",
    "Zoom": "zoom",
    "Firefox": "firefox"
    # ["",""],["",""],["",""],["",""],

    # Add more applications and their process names as needed
}


def close_app(query):
    Say("closing, sir")
    """
    Close applications based on user query.
    """
    # Iterate through the dictionary of applications and process names
    for app_name, process_name in app_process_names.items():
        # Check if the query contains the name of an application to close
        if f"close {app_name}".lower() in query.lower():
            try:
                # Use the taskkill command to close the application
                # '/f' option forces the termination
                # '/im' option specifies the image name (process name) to close
                os.system(f"taskkill /f /im {process_name}")
                Say(f"Closed {app_name}.")
                return
            except Exception as e:
                # Provide feedback in case of an error
                Say(f"Failed to close {app_name}. Error: {e}")
                return

    # Handle closing tabs in browsers using pyautogui
    if "close tab" in query:
        # You can adjust the number of times to close tabs based on user query
        num_tabs = 1  # Default to closing one tab
        try:
            if "one tab" in query or "1 tab" in query:
                num_tabs = 1
            elif "two tabs" in query or "2 tabs" in query:
                num_tabs = 2
            elif "three tabs" in query or "3 tabs" in query:
                num_tabs = 3
            # Add more cases if needed

            for _ in range(num_tabs):
                # Use pyautogui to close the specified number of tabs
                pyautogui.hotkey("ctrl", "w")
            Say(f"Closed {num_tabs} tab(s).")
        except Exception as e:
            Say(f"Failed to close tab(s). Error: {e}")
    else:
        Say("Sorry, I didn't recognize the application to close.")

# Example usage:
# close_app("close vscode")
# close_app("close tab")
