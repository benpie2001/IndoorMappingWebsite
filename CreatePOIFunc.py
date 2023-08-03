import requests

AuthKey = 'AUTHKEY GOES HERE'

url = 'MAPS INDOORS URL'
headers = {'authorization': AuthKey, 
           'accept': 'application/json', 
           'Content-Type': 'application/json'}

def CreatePOI(LongLat):
    data = [{'parentId': 'PARENTID goes here',
             'datasetId': 'DATASETID goes here',
             'baseType': 'poi',
             'displayTypeId': 'DISPLAYTYPEID goes here',
             'geometry': {'coordinates': LongLat, 'type': 'Point'},
             'anchor': {'coordinates': LongLat, 'type': 'Point'},
             'aliases': [],
             'categories': [],
             'status': 3,
             'properties': {'name@en': 'User'}}]
    UserId = requests.post(url, headers=headers, json=data)
    UserId.dict = UserId.json()
    return UserId.dict