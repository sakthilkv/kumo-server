import os
import requests
import json


class JikanAPIHandler:
    def request(self,url):
        
        response = requests.get("https://api.jikan.moe/v4/anime" + url)

        if response.status_code == 200:
            return response.json()
        else:
            return {}