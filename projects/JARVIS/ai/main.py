import requests
from functions.online_ops import find_my_ip, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from functions.online_ops import get_latest_news
from graphics import *
from decouple import config
from datetime import datetime
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad
from hashlib import *
from tkinter import *
#from speech_rec import take_user_input
from speech_rec import speak

app()
USERNAME = config('USER')
BOTNAME = config('BOTNAME')
LOGIN=config("SHA-512")

#temp input method.
def take_user_input():
    query=input("COMMAND: ")
    return query

# Greet the user
def greet_user():
    speak("Welcome Back Sir",1)

if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input()

        if 'notepad'in query:
            open_notepad()

        elif 'jarvis' in query:
            speak("Yes sir?",1)

        elif 'command prompt' in query or 'command' in query:
            open_cmd()

        elif 'camera' in query:
            open_camera()

        elif 'calculator' in query:
            open_calculator()
        
        elif 'time' in query or 'date' in query:
            speak(datetime.today().strftime('it is %H:%M on %m-%d-%Y'),0)
            speak("For your convenience, I have printed it on the screen sir.",1)

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?',1)
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}",0)
            speak("For your convenience, I have printed it on the screen sir.",1)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?',1)
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'ip' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}',0)
            speak('For your convenience, I have printed it on the screen sir.',1)

        elif "whatsap" in query:
            speak('On what number should I send the message sir? Please enter in the console: ',1)
            number = input("Enter the number: ")
            speak("What is the message sir?",1)
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.",1)

        elif "email" in query:
            speak("To what email address do I send sir? Please enter in the console: ",1)
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?",1)
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.",1)
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.",1)

        elif 'joke' in query:
            speak(f"Hope you like this one sir",1)
            joke = get_random_joke()
            speak(joke,0)
            speak("For your convenience, I have printed it on the screen sir.",1)

        elif "advice" in query:
            speak(f"Here's some advice for you, sir",1)
            advice = get_random_advice()
            speak(advice,0)
            speak("For your convenience, I have printed it on the screen sir.",1)

        elif "movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}",0)
            speak("For your convenience, I have printed it on the screen sir.",1)

        elif 'news' in query:
            speak(f"I'm reading out some of the latest news headlines, sir",1)
            speak(get_latest_news(1),0)
            speak(get_latest_news(2),0)
            speak(get_latest_news(3),0)
            speak(get_latest_news(4),0)
            speak(get_latest_news(5),0)
            speak("For your convenience, I have printed it on the screen sir.",1)

        elif 'weather' in query:
            speak(f"Getting weather report for your city {city}",1)
            city, weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}",0)
            speak(f"Also, the weather report talks about {weather}",0)
            speak("For your convenience, I have printed it on the screen sir.",1)

        
