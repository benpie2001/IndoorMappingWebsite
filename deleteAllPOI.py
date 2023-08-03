import requests
from DeletePOIFunc import *

url = 'MAPSINDOORS URL GOES HERE'
Deleteheaders = {'accept': 'application/json'}

def DeleteAllPOI():
    r = requests.get(url, headers=Deleteheaders)
    r_dict = r.json()
    for poi in r_dict:
        if poi['displayTypeId'] == 'DISPLAYTYPEID goes here':
            poiId = poi['id']
            DeletePOI(poiId)
            print("USER DELETED")

DeleteAllPOI()