from datetime import datetime
import pyttsx3
import speech_recognition as sr
from graphics import *

engine = pyttsx3.init('sapi5')
listener = sr.Recognizer()

# Set Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)


# Text to Speech Conversion
def speak(text, bin):
    if bin==0:
        engine.say(text)
        engine.runAndWait()
        jprint(text)
    elif bin==1:
        engine.say(text)
        engine.runAndWait()
    else: print("Invalid")

#Takes Input from User
def take_user_input():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            query=listener.recognize_google(voice)
            query.lower()
        if not 'exit' in query or 'stop' in query:
            speak("")
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query