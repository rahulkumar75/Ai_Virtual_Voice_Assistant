import speech_recognition as sr

def listen():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the source for input
    with sr.Microphone() as source:
        print("Listening for commands...")

        # Adjust for ambient noise and record audio from the microphone
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Recognize the speech using Google Web Speech API
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    return None

def main():
    while True:
        command = listen()
        if command:
            if "stop listening" in command.lower():
                print("Stopping listening as per command.")
                break
            # You can add more command handling logic here
            elif "hello" in command.lower():
                print("Hello! How can I assist you today?")
            # Add more commands as needed

if __name__ == "__main__":
    while True:
        main()
