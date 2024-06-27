from Speak import Say
import datetime

def greetMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour <= 12:
        Say("Good Morning")

    elif 12 < hour <= 18:
        Say("Good Afternoon")

    else:
        Say("Good evening")

    Say("Please tell me, How can I help you ? ")

# greetMe()

