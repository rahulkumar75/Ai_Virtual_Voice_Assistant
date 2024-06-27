import requests
from Speak import Say
from requests import get

def find_my_ip():
    Say("Finding IP Address")
    ip_address = requests.get('https://api.ipify.org?format=json').json()
    result = ip_address["ip"]

    Say("Your IP Address is: " + result)
    return result



# find_my_ip()



















