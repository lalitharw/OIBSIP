from dotenv import load_dotenv
import os
import requests

load_dotenv()

# reading api key from .env file
API_KEY = os.getenv("API")

def formatDisplay(response):
    # converting kelvin to Celsius 
    temperature_conversion = response['main']['temp'] - 273.15

    # converting m/s to km/h
    speed_conversion = response['wind']['speed']  * 3.6
    print(f"Weather Information for city {response['name']}: \nTemperature: {temperature_conversion: .1f} \u00b0C\nHumidity: {response['main']['humidity']} %\nWeather Condition: {response['weather'][0]['description']}\nWind Speed: {speed_conversion: .2f} km/h")

def displayWeather(city):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    response = requests.get(url).json()
    # checking if status_code is 200
    if(response['cod'] == 200):
        # function to display information in neat format
        formatDisplay(response)
    else:
        print("Invalid City! Please enter valid City")


while(1):
    CITY = input("Enter city's weather you want to check (Q to Quit):").lower()
    if CITY == "q":
        break
    else:
        displayWeather(CITY)


