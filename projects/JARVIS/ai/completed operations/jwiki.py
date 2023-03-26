from wikipedia import *
from speak import *
from listen import *

def search_on_wikipedia(value):
    try:
        p=wikipedia.summary(value, auto_suggest=False, sentences=2)
        return p
    except exceptions.DisambiguationError as e:
        print(e)
        s=input("How do you want to refine your search? ")
        p=wikipedia.summary(s, auto_suggest=False,sentences=2)
        return p
    

speak('What do you want to search on Wikipedia, sir?')
search_query = input(":")
results = search_on_wikipedia(search_query)
speak(f"According to Wikipedia, {results}",0)
speak("For your convenience, I have printed it on the screen sir.")

#print(search_on_wikipedia("python"))