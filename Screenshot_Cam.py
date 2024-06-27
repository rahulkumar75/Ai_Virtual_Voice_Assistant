import pyautogui
from Speak import Say



def take_photo():
    """
    Take a photo using the camera application
    """
    try:
        Say("Opening the camera app, please wait...")
        # Open the camera app on Windows
        pyautogui.press("super")  # Windows key
        pyautogui.typewrite("camera")
        pyautogui.press("enter")

        # Add a delay to allow the camera app to open
        pyautogui.sleep(5)  # Adjust the time as needed

        # Announce to smile
        Say("SMILE PLEASE...")

        # Press the enter key to take the photo
        pyautogui.press("enter")

        Say("Photo taken.")

    except Exception as e:
        Say(f"No command to take a photo recognized. {e}")


def screenshot():

        try:
            # Take a screenshot and save it as a file
            im = pyautogui.screenshot()
            im.save("screenshot_sample.jpg")
            Say("Screenshot captured and saved.")

        except Exception as e:
            Say(f"Failed to capture screenshot. Error: {e}")


# screenshot()