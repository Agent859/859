import pywhatkit as kit
from speak import *
from listen import *

def search_on_google(query):
    kit.search(query)

#speak('What do you want to search on Google, sir?')
#query = listen().lower()
#search_on_google(query)

search_on_google("test")