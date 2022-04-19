"# SoundTinder" 
"# soundtinder" 
## Setup Instructions to run locally
1. `pip3 install -r requirements.txt`
2. Create a `.env` file in the top-level directory and enter the following as its contents:
```
export DATABASE_URL="<YOUR POSTGRESQL DB URL>"
export SECRET_KEY="<MAKE UP A SECRET KEY>"
export GOOGLE_CLIENT_ID="<GOOGLE CLIENT ID FROM GOOGLE CLOUD CONSOLE>"
export GOOGLE_CLIENT_SECRET="<GOOGLE CLIENT SECRET KEY FROM GOOGLE CLOUD CONSOLE>"
```
3. comment out lines that contain 'IP' and 'PORT' in routes.py so google oauth will work
4. Run `python3 routes.py`

