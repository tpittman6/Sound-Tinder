## Setup Instructions
1. `pip3 install -r requirements.txt`
2. Create a `.env` file in the top-level directory and enter the following as its contents:
```
export TMDB_API_KEY="<YOUR API KEY>"
export DATABASE_URL="<YOUR POSTGRESQL DB URL>"
```


## To run the app
1. Run `python3 routes.py`

"# SoundTinder" 
"# soundtinder" 
1. Follow [this tutorial](https://developer.spotify.com/web-api/tutorial/) to create your own Spotify App. Then add "http://127.0.0.1:8081/callback/" as a redirect URI.  

2. Create a file named **conf.json** in this folder with the exact same structure of the conf_example.json file
