import pyautogui
from Speak import Say
from Listen import Listen


def youtubeControl(query):

    if "pause" in query:
        pyautogui.press("k")
        Say("video paused")

    elif "play" in query:
        pyautogui.press("k")
        Say("video played")

    elif "mute" in query:
        pyautogui.press("m")
        Say("video muted")

    elif "unmute" in query:
        pyautogui.press("m")
        Say("video unmuted")

    elif "volume up" in query:
        from keyboard import volumeup
        Say("turning volume up,sir")
        volumeup()

    elif "volume down" in query:
        from keyboard import volumedown
        Say("Turning volume down,sir")
        volumedown()