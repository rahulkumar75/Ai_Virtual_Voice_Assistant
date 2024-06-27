import pyttsx3  # pip install pyttsx3

# Initialize the text-to-speech engine once at the start
engine = pyttsx3.init("sapi5")

# Set the voice properties once
voices = engine.getProperty('voices')

# Set the desired voice (e.g., the first voice in the list)
engine.setProperty('voice', voices[0].id)

# Set the speech rate
engine.setProperty('rate', 170)


def Say(text):
    try:
        # Output the text being spoken
        print(f"A.I: {text}")

        # Use the engine to say the text
        engine.say(text)

        # Run the text-to-speech synthesis
        engine.runAndWait()
        print("")

    except Exception as e:
        print(f"An error occurred during text-to-speech synthesis: {e}")
        Say("Sorry, an error occurred while speaking.")

