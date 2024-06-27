import speech_recognition as sr  # pip install speechrecognition
from colorama import init, Fore, Back, Style  # pip install colorama

# Initialize colorama
init()

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(Fore.LIGHTBLUE_EX + "Listening...")
        r.pause_threshold = 1

        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 100
        audio = r.listen(source, 0, 4)

    try:
        print(Fore.YELLOW + "Recognizing...")
        print("")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said : {query}")
        print("")

    except sr.RequestError as e:
        print(Fore.RED + "Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

    except:
        print(Fore.RED + "Sorry, I could not understand your speech. Please try again.")
        print("")
        return ""

    query = str(query)
    return query.lower()

# Listen()