import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather_condition(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if "weather" in data:
        return data["weather"][0]["main"]
    return "Clear"
