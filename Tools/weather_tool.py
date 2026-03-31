from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

Weather_API_KEY = os.getenv("OPENWEATHER_API_KEY")

@tool("weather")
def weather_agent(city):
    """Get current weather information including temperature,
humidity, and wind speed for a given city."""

    url= f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Weather_API_KEY}&units=metric" 
    
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] != 200:
        return "City not found.Please try again.!!!"
    
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humid = data["main"]["humidity"]
    windSpeed = data['wind']['speed']
    
    return f"The temperature in {city} is {temp}°C with {description} recording a humidity of {humid} with a WindSpeed of {windSpeed}"