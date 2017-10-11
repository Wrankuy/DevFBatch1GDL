import requests

url = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE')
response = requests.get(url)

print response.json()

print response.text

class X(object):
    def __init__(self, X_object):
        self.html_atm = X_object
        self.results = X_object





