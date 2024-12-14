import json

from flask import jsonify
from app.core import TMDbAPIHandler as TMDB
from app.models import Record
class AnimeController:
    handler = TMDB()
    @staticmethod
    def get_min_anime_info(id):
        data = AnimeController.handler.request(f"tv/{id}")
        if data:
            response = {
                "id": data["id"],
                "media_type": "anime",
                "title": data["name"],
                "poster_url": data["poster_path"],
                "year": data["first_air_date"].split('-')[0]
            }
            return response

        return  {}
    def get_anime_info(id,uid):
        data = AnimeController.handler.request(f"tv/{id}")
        if data:
            status = Record.check_media_status(uid=uid,media_type="anime",media_id=id)
            if not status:
                status = "none"
            else:
                status = str(status.status)
            if  "16" in [str(genre["id"]) for genre in data["genres"]] or any(country in ["JP", "CN", "KR"] for country in data["origin_country"]):
                response = {
                    "cbfc": "A" if data["adult"] else "U",
                    "genre": [str(genre["id"]) for genre in data["genres"]],
                    "id": str(data["id"]),
                    "media_type": "anime",
                    "runtime": data["last_episode_to_air"]["runtime"] if data("last_episode_to_air",None) else "0",
                    "title": data["name"],
                    "plot": data["overview"],
                    "poster_url": data["poster_path"],
                    "release_date": data["first_air_date"],
                    "status": str(status)
                }
                return response
            else:
                return jsonify({"message": "sorry :("}), 400
        else:
            return jsonify({"message": "sorry"}), 400
    
    def search_anime(keyword):
        data = AnimeController.handler.request(f"search/tv?query={keyword}&include_adult=true").get("results",None)
        if data:
            response = {"results":[]}
            for result in data:
                if result["poster_path"] and (16 in result["genre_ids"] and any(country in ["JP", "CN", "KR"] for country in result["origin_country"])):
                    response["results"].append({
                        "id": result["id"],
                        "title":result["name"],
                        "media_type": "anime",
                        "poster_url":str(result["poster_path"]),
                        "year": result["first_air_date"].split('-')[0]
                    })
            return response
        else:
            return {}

