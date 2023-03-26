import os
import socket
import requests

def find_my_ip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr

def get_weather_report(n):
    city = requests.get("https://geolocation-db.com/json/39.110.142.79&position=true").json()
    weather = os.system(f'curl wttr.in/{city}?format="%C"')
    temperature = os.system(f'curl wttr.in/{city}?format="%t"')
    feels_like = os.system(f'curl wttr.in/{city}?format="%f"')
    report=[city, weather, temperature, feels_like]
    return report[n]

def whether():
    city = get_weather_report(0)
    print(f"Getting weather report for your city, {city}")
    print(f"The skyies are {get_weather_report(1)}, with temperatrues at {get_weather_report(2)}, but it feels like {get_weather_report(3)}")
    print("For your convenience, I have printed it on the screen sir.")

print(find_my_ip())
whether()