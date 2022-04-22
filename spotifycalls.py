import os
import string
import app
from urllib import response
from dotenv import find_dotenv, load_dotenv
import requests
import base64
import json

load_dotenv(find_dotenv())

api_url_artist = "https://api.spotify.com/v1/artists/"
api_token_url = "https://accounts.spotify.com/api/token"

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# all comments below are just tests to see what went wrong with the API call.
# UNIT TESTING STILL REQUIRED
def authorize():
    DATA = {
        "Content-Type": "application/x-www-form-urlencoded",
        "grant_type": "client_credentials",
    }

    authkeydata = requests.post(
        api_token_url, auth=(CLIENT_ID, CLIENT_SECRET), data=DATA
    )
    reqkey = authkeydata.json()
    token = reqkey.get("access_token")
    # print(token)
    return f"{token}"


def artist_basic_info(artistID):
    ART_URL = api_url_artist + artistID
    # print("1")
    headers = {
        "Authorization": f"Bearer {authorize()}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    # print("2")
    res = requests.get(ART_URL, headers=headers)
    art_data = res.json()
    # print(art_data)


artist_basic_info("5f7VJjfbwm532GiveGC0ZK")
