import requests

AuthKey = 'AUTHKEY GOES HERE'

url = 'MAPS INDOORS URL'
headers = {'authorization': AuthKey, 
           'accept': '*/*', 
           'Content-Type': 'application/json'}

def UpdatePOI(POItoChange, NewLongLat):
    data = [{'id': POItoChange,
             'geometry': {'coordinates': NewLongLat, 'type': 'Point'},
             'anchor': {'coordinates': NewLongLat, 'type': 'Point'}}]
    r = requests.put(url, headers=headers, json=data)
    return r
