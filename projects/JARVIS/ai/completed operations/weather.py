from pywttr import Wttr
from speak import speak

def get_local_weather(city):
    wttr=Wttr(city)
    forecast = wttr.en()
    high = forecast.weather[1].maxtemp_f
    rain=forecast.weather[1].hourly[1].chanceofrain
    temp=forecast.weather[1].hourly[1].temp_f
    feel=forecast.weather[1].hourly[1].feels_like_f
    return (f"The high today in {city} is {high} degrees. There is a {rain}% chance of rain. The current temperature is {temp} degrees, but it feels like {feel}")

city="Merced"
print(get_local_weather(city))
speak(get_local_weather(city))