from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

Weather_API_KEY = st.secrets["OPENWEATHER_API_KEY"]

@tool
def weather_agent(city: str):
    """Get current weather information including temperature,
    humidity, and wind speed for a given city."""

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Weather_API_KEY}&units=metric"

    try:
        response = requests.get(url)
        
        # ❗ Check HTTP status
        if response.status_code != 200:
            return {"error": f"HTTP Error: {response.status_code}"}

        data = response.json()

        # ❗ API-level error
        if str(data.get("cod")) != "200":
            return {"error": "City not found"}

        # Extract data safely
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humid = data["main"]["humidity"]
        windSpeed = data["wind"]["speed"]

        return {
            "city": city,
            "temp": temp,
            "description": description,
            "humidity": humid,
            "wind_speed": windSpeed
        }

    except Exception as e:
        return {"error": str(e)}