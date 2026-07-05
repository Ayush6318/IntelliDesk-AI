import os
import requests

from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


@tool
def weather(city: str) -> str:
    """
    Get the current weather for a given city.
    """

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(url, params=params)

        response.raise_for_status()

        data = response.json()

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        return (
            f"Weather in {city}:\n"
            f"Temperature: {temperature}°C\n"
            f"Condition: {description}\n"
            f"Humidity: {humidity}%"
        )

    except requests.exceptions.HTTPError:
        return f"Could not find weather information for '{city}'."

    except Exception as e:
        return f"Weather service error: {e}"
    
if __name__ == "__main__":
    print(weather.invoke({"city": "Delhi"}))