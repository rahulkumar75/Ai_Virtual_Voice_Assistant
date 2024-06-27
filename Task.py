# Functions
import datetime
import requests
import os
import pywhatkit
from Speak import Say
from googletrans import Translator
from Listen import Listen
from Dictapp import openappweb
import credential
from time import sleep


# 2-Types
# i) Non Input eg: Date, Time,Speed Test
# ii)Input eg: Google search, wikipedia

# ******************************************************* NoN Input Wala Task
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)


def Date():
    date = datetime.date.today()
    Say(date)


def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    advice = res['slip']['advice']
    print(advice)


def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


def internet_speed():
    from Speedtest import get_speedtest
    get_speedtest()


def Movies():
    from MoviesDetails import moviesInfo
    moviesInfo()


def News():
    from NewHeadline import get_latest_news
    get_latest_news()


def WhatsApp():
    Say("Enter the Phone Number")
    number = input("Enter Mob. Number:")
    Say("Please Tell the Message Here:")
    user_message = Listen()
    sleep(0.2)
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", user_message)
    Say("Message Sent Successfully!")


def Temperature():
    from Temperature import get_weather
    print('Enter The Location')
    city_name = input()
    api_key = credential.temp_api_key

    get_weather(city_name, api_key)


def alarm():
    from Alarm import handle_alarm
    handle_alarm()


# --------------------------------------------------------------
def NonInputExecution(query):
    query = str(query)
    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

    elif "random advice" in query:
        get_random_advice()

    elif "internet speed" in query:
        internet_speed()

    elif "screenshot" in query:
        from Screenshot_Cam import screenshot
        screenshot()

    elif "take my photo" in query:
        from Screenshot_Cam import take_photo
        take_photo()

    elif "game" in query:
        from game import game_play
        game_play()

    elif "ip address" in query:
        from IP_Adderess import find_my_ip
        find_my_ip()

    elif "shutdown system" in query:
        from Shutdown_PC import handle_shutdown
        handle_shutdown()
    elif "play" in query:
        from youtubeControl import youtubeControl
        youtubeControl("play")

    elif "pause" in query:
        from youtubeControl import youtubeControl
        youtubeControl("pause")

    elif "mute" in query:
        from youtubeControl import youtubeControl
        youtubeControl("mute")

    elif "unmute" in query:
        from youtubeControl import youtubeControl
        youtubeControl("unmute")

    elif "volume up" in query:
        from youtubeControl import youtubeControl
        youtubeControl("volume up")

    elif "volume down" in query:
        from youtubeControl import youtubeControl
        youtubeControl("volume down")

    elif "remember that" in query:
        from Remember import memorize_query
        memorize_query("remember that")

    elif "do you remember anything" in query:
        from Remember import memorize_query
        memorize_query("do you remember anything")


# ---------------------------------------------------------------
def InputExecution(tag, query):
    if "change password" in tag:
        from Password_Change import change_password
        change_password()

    if "wikipedia" in tag:
        from SearchNow import searchWikipedia
        searchWikipedia(query)

    elif "search on google" in tag:
        from SearchNow import searchGoogle
        searchGoogle(query)

    elif "search on youtube" in query:
        from SearchNow import searchYoutube
        searchYoutube(query)

    elif "translate" in tag:
        print("What would you like to translate?")
        text_to_translate = Listen()
        print(text_to_translate)
        print("To which language?")
        target_language = Listen()
        print(target_language)
        translated_text = translate_text(text_to_translate, target_language)
        # print("Translated text:", translated_text)
        Say(translated_text)

    elif "movie" in tag:
        Movies()

    elif "news" in tag:
        News()

    elif "whatsapp" in tag:
        WhatsApp()

    elif "temperature" in tag:
        Temperature()

    elif "open" in tag:
        openappweb(query)

    elif "close" in tag:
        from closeApp import close_app
        close_app(query)

    elif "remember that" in query:
        Say("What should I remember")
        data = Listen()
        Say("You said me to remember that" + data)
        print("You said me to remember that " + str(data))
        remember = open("RememberData.txt", "w")
        remember.write(data)
        remember.close()

    elif "do you remember anything" in query:
        remember = open("RememberData.txt", "r")
        Say("You told me to remember that" + remember.read())
        print("You told me to remember that " + str(remember))

    elif "alarm" in tag:
        alarm()


    elif "ai image" in tag:
        from ai_Image_generetor import generator_image
        generator_image()

    elif "set schedule" in tag:
        from Schedule_My_Day import clear_old_tasks
        clear_old_tasks()

    elif "show my schedule" in tag:
        from Schedule_My_Day import show_schedule
        show_schedule()

    elif "send email" in tag:
        from SendEmail import send_mail
        send_mail()

