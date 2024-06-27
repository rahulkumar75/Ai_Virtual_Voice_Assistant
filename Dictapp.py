import os
import subprocess
from AppOpener import open
import pyautogui
import webbrowser
from Speak import Say
from time import sleep
from Listen import Listen


# Define a list of websites and their URLs
sites = [
    ["youtube", "youtube.com"],
    ["facebook", "facebook.com"],
    ["udemy", "udemy.com"],
    ["instagram", "instagram.com"],
]

# Define a list of applications and their commands
dictapp = [
    ["paint", "mspaint"],
    ["commandprompt", "cmd"],
    ["word", "winword"],
    ["excel", "excel"],
    ["chrome", "C:Program Files\\Google\\Chrome\\Application\\chrome.exe"],
    ["vscode", "C:\\Users\\rahul\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"],
    ["powerpoint","powerpnt"],
    ["Notepad", "notepad"],
    ["Calculator","calc"],
    ["powerpoint", "powerpoint"],
    ["File Explorer","explorer"],
    ["Microsoft Edge","msedge"],
    ["Google Chrome","chrome"],
    ["VLC Media Player","vlc"],
    ["Spotify","spotify"],
    ["Zoom","zoom"],
    ["Firefox","firefox"],
    # ["",""],["",""],["",""],["",""],
]

def open_website(query):
    """
    Open websites based on user query.
    """
    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            Say(f"Opening {site[0]}...")
            webbrowser.open(f"https://{site[1]}")
            return True
    return False

def open_application(query):
    """
    Open applications based on user query.
    """
    for app in dictapp:
        if f"open {app[0]}".lower() in query.lower():
            Say(f"Opening {app[0]}...")
            try:
                # Use subprocess.Popen() instead of os.system() for better control and consistency
                # subprocess.Popen(app[1])
                os.startfile(app[1])
                return True
            except Exception as e:
                Say(f"Failed to open {app[0]}. Error: {e}")
                return False
    return False

def open_dynamic_url(query):
    """
    Open dynamic URLs based on user query.
    """
    if any(extension in query for extension in [".com", ".co.in", ".org"]):
        query = query.replace("open", "").strip()
        query = query.replace("jarvis", "").strip()
        query = query.replace("launch", "").strip()
        query = query.replace(" ", "")
        webbrowser.open(f"https://{query}")
        Say(f"Opening {query}...")
        return True
    return False

def openappweb(query):
    """
    Main function to handle opening websites and applications based on user query.
    """
    if open_website(query) or open_application(query) or open_dynamic_url(query):
        return
    else:
        Say("Sorry, I didn't recognize that command.")

# ------------------------------------------------------------ CLOSE APP
# def closeappweb(query):
#     Say("Closing, sir")
#     from closeApp import close_app
#     close_app(query)

# EX:
# openappweb("open VLC Media Player")