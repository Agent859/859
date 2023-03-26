import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')

# Set Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)

# Text to Speech Conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()