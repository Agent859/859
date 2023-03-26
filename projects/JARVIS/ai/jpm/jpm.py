from webbot import *
from robobrowser import RoboBrowser 
from pykeepass import *

def get_username(text):
    kp = PyKeePass("D:\Projects\jarvis\jpm\jarvis.kdbx", password='Syfrett66678597!')
    entry = kp.find_entries(title=text, first=True)
    username=entry.username
    return print(username)

def get_password(text):
    kp = PyKeePass("D:\Projects\jarvis\jpm\jarvis.kdbx", password='Syfrett66678597!')
    entry = kp.find_entries(title=text, first=True)
    password = entry.password
    return print(password)

def get_url(text):
    kp = PyKeePass("D:\Projects\jarvis\jpm\jarvis.kdbx", password='Syfrett66678597!')
    entry = kp.find_entries(title=text, first=True)
    link = entry.url
    return print(link)

get_username("Sample Entry #2")
get_password("Sample Entry #2")
get_url("Sample Entry #2")

def sign_in(text):
    browser = RoboBrowser() 
    login_url = get_url(text)
    browser.open(login_url) 
    form = browser.get_form(id='form_id') 
    form['username'].value = get_username(text) 
    form['password'].value = get_password(text)
    browser.submit_form(form)

sign_in("Sample Entry #2")