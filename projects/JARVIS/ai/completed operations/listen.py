from datetime import datetime
import speech_recognition as sr
from speak import speak

listener = sr.Recognizer()

#Takes Input from User
def listen():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            query=listener.recognize_google(voice)
            query.lower()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return print(query)
