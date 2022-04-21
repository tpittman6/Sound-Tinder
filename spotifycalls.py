import os
from dotenv import find_dotenv, load_dotenv
import requests
import base64
import json

load_dotenv(find_dotenv())

api_url = "https://api.spotify.com/v1/artists/"
api_token_url = "https://accounts.spotify.com/api/token"

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
payload = {
    "Content-Type": "application/x-www-form-urlencoded",
    "grant_type": "client_credentials",
}


res = requests.post(api_token_url, auth=(CLIENT_ID, CLIENT_SECRET), data=payload)
res_data = res.json()

print(res_data)


# def api_access_token():
#    token_response = requests.post(
#    )
# def artist_basic_info(artistID):
