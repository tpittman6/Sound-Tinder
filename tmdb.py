import os
import requests
import base64
import random
import json

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

IMAGE_BASE_URL = "https://image.tmdb.org/t/p/"
POSTER_SIZE = "w500"


def get_movie_data(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}",
        params={
            "api_key": os.getenv("TMDB_API_KEY"),
        },
    )
    json_response = response.json()
    title = json_response["title"]
    tagline = json_response["tagline"]
    genres = ", ".join(genre["name"] for genre in json_response["genres"])
    poster_path = json_response["poster_path"]
    poster_image = f"{IMAGE_BASE_URL}/{POSTER_SIZE}{poster_path}"
    return (title, tagline, genres, poster_image)
