from Speak import Say
import requests
import credential


# def convert_timestamp(timestamp):
#     # Convert the timestamp to a datetime object
#     dt_object = datetime.utcfromtimestamp(timestamp)
#
#     # Convert the datetime object to a readable date and time format
#     readable_date_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
#     # readable_date_time = dt_object.strftime('%H:%M:%S')
#
#     return readable_date_time

# Function to get weather updates
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        min_temperature = str(data["main"]["temp_min"])
        max_temperature = str(data["main"]["temp_max"])
        humidity = data["main"]["humidity"]

        Say(f"The current temperature in {city} is {temperature}°C with {weather_description}.")
        print(f"The current temperature in {city} is {temperature}°C with {weather_description}.")
        print("Min_temp: " + min_temperature + "    " + "Max_Temp: " + max_temperature)

        # Convert the timestamp and print the result
        # sunrise = convert_timestamp(data["sys"]["sunrise"])
        # print(f"Sunrise: {sunrise}")
        # sunset = convert_timestamp(data["sys"]["sunset"])
        # print(f"Sunset: {sunset}")

    else:
        Say(f"Sorry, I couldn't find weather information for {city}.")


# Given timestamp in seconds since Unix epoch
# timestamp = 1713829756
