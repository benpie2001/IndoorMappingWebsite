import numpy as np

def XYtoLatLongFunc(userX, userY):
    Xdelta = userX/(111111*(np.cos(np.radians(41.8044348))))
    Ydelta = userY/111111
    latitude = 41.8044348 + Ydelta
    longitude = -72.2571437 + Xdelta
    return [latitude, longitude]