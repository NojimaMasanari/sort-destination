import requests
from .config import GOOGLE_API_DIRECTIONS, GOOGLE_API_GEOCODE, GURUNAVI_API
from .config import GOOGEL_APIKEY, GURUNAVI_APIKEY


def get_center_latlng(keyword):
    url = GOOGLE_API_GEOCODE % (
        keyword, GOOGEL_APIKEY)
    resp = requests.get(url)
    json = resp.json()
    if json["status"] == "OK":
        location = json["results"][0]["geometry"]["location"]
        return location
    else:
        return False


def gurunavi_info(center_latlng, freeword):
    lat = center_latlng["lat"]
    lng = center_latlng["lng"]
    url = GURUNAVI_API % (
        GURUNAVI_APIKEY, lat, lng, 2, freeword)
    resp = requests.get(url)
    json = resp.json()
    return json


def get_distance(start, end):
    url = GOOGLE_API_DIRECTIONS % (
        start, end, GOOGEL_APIKEY)
    resp = requests.get(url)
    json = resp.json()
    if json["status"] == "OK":
        info = json["routes"][0]["legs"][0]
        return info
    else:
        # print("json: ",json)
        return False
