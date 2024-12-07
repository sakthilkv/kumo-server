import os
import requests
import json

# from dotenv import load_dotenv
# load_dotenv()

TMDB_TOKEN = os.getenv("TMDB_TOKEN")

class TMDbAPIHandler:
    def request(self,url):
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TMDB_TOKEN}"
        }
        response = requests.get("https://api.themoviedb.org/3/" + url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return {}
    
# handler = TMDbAPIHandler()
# url = "https://api.themoviedb.org/3/movie/324857"
# data = handler.send_request(url)
# print(data)
