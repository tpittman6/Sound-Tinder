import os
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
DATA = {
    "Content-Type": "application/x-www-form-urlencoded",
    "grant_type": "client_credentials",
}


authkeydata = requests.post(api_token_url, auth=(CLIENT_ID, CLIENT_SECRET), data=DATA)
reqkey = authkeydata.json()
token = reqkey.get("access_token")


def artist_basic_info(artistID):
    res = response.get
