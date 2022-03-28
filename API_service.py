import requests
BASE_URL = "http://kontests.net/api/v1/"


# Used in API-commands.py for each command
def fetch(suffix):
    res = requests.get(BASE_URL+suffix)
    data = res.json()
    return data


