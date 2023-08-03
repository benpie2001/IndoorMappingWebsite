import requests

AuthKey = 'AUTHKEY GOES HERE'

url = 'MAPS INDOORS URL'
headers = {'authorization': AuthKey, 
           'accept': '*/*', 
           'Content-Type': 'application/json'}

def DeletePOI(POItoDelete):
    data = [POItoDelete]
    r = requests.delete(url, headers=headers, json=data)
    return r