import os
import requests
from wikipedia import *
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
from random import *
#from speech_rec import *

#temp input method
def take_user_input():
    query=input("COMMAND: ")
    return query

NEWS_API_KEY = config("NEWS_API_KEY")
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
TMDB_API_KEY = config("TMDB_API_KEY")
EMAIL = "rogue.ms.2021@gmail.com"
PASSWORD = "Syfrett801"


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def search_on_wikipedia(value):
    try:
        p=wikipedia.summary(value, auto_suggest=False, sentences=2)
        return p
    except exceptions.DisambiguationError as e:
        print(e)
        s=take_user_input()
        p=wikipedia.summary(s, auto_suggest=False,sentences=2)
        return p


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+1{number}", message)


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

send_email("infernofire859@proton.me", "Test", "Testing")

def get_latest_news(num):
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[num]

def get_weather_report():
    city = requests.get(f"https://ipapi.co/{find_my_ip()}/city/").text
    weather = os.system(f'curl wttr.in/{city}?format="%C"')
    temperature = os.system('curl wttr.in/{city}?format="%t"')
    feels_like = os.system('curl wttr.in/{city}}?format="%f"')
    return weather, f"{temperature}℃", f"{feels_like}℃"

def get_trending_movies():
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


