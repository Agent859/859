import requests

def get_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def get_city():
    city = requests.get(f"https://ipapi.co/{get_ip()}/city/").text
    return city
print(get_city())