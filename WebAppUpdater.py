from CreatePOIFunc import *
from DeletePOIFunc import *
from UpdatePOIFunc import *
from TrackerAPI import *
from XYtoLatLong import *

initialTrackerTime = 0
startTime = time.time()

savedUsers = {}
currentPOIs = []
usersToDelete = []

while True:
    Tracker = CCTracker()
    User_Count = Tracker['count']
    if User_Count != 0:
        trackerTime = Tracker['users'][0]['timestamp']
        if trackerTime != initialTrackerTime:
            trackedUsers = Tracker['users']
            for user in trackedUsers:
                if user['identifier'] not in savedUsers:
                    Xcoord = user['x']
                    Ycoord = user['y']
                    LatLong = XYtoLatLongFunc(Xcoord, Ycoord)
                    MapId = CreatePOI([LatLong[1], LatLong[0]])
                    print("USER ADDED")
                    currentPOIs.append(MapId[0])
                    savedUsers.update({user['identifier']: MapId[0]})
                    print(savedUsers)
                else:
                    Xcoord = user['x']
                    Ycoord = user['y']
                    LatLong = XYtoLatLongFunc(Xcoord, Ycoord)
                    MapId = savedUsers[user['identifier']]
                    UpdatePOI(MapId, [LatLong[1], LatLong[0]])
                    print("USER UPDATED")
                    currentPOIs.append(MapId)
            for user in savedUsers:
                if savedUsers[user] not in currentPOIs:
                    DeletePOI(savedUsers[user])
                    print("USER DELETED")
                    usersToDelete.append(user)
            for garbage in usersToDelete:
                savedUsers.pop(garbage)
            currentPOIs = []
            usersToDelete = []
            initialTrackerTime = trackerTime
    else:
        print("NO USERS FOUND")
        for user in savedUsers:
                DeletePOI(savedUsers[user])
                print("USER DELETED")
                usersToDelete.append(user)
        for garbage in usersToDelete:
            savedUsers.pop(garbage)
        currentPOIs = []
        usersToDelete = []
        time.sleep(30.0 - ((time.time() - startTime) % 30.0))