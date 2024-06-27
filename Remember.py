from Speak import Say
from Listen import Listen

def memorize_query(query):

    try:
        if "remember that" in query:
            Say("What should I remember")
            data = Listen()
            Say("You said me to remember that " + data)
            remember = open("RememberData.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("RememberData.txt", "r")
            Say("You told me to remember that " + remember.read())

    except:
        print("error found in Remember.py File")
