import requests
import time
import json

def current_milli_time():
    return round(time.time() * 1000)

url = 'CROWDCONNECTED API URL'
headers = {'Auth': 'AUTHKEY GOES HERE', 'Content-Type': 'application/json'}

def CCTracker():
    data = {'atTime': current_milli_time(), "identifiers": [], "maxAge": 90000}
    r = requests.post(url, headers=headers, json=data)
    r_dict = r.json()
    return r_dict
