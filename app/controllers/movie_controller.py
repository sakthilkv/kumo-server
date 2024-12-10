import json

from flask import jsonify
from app.core import TMDbAPIHandler as TMDB
from app.models.record_model import Record

class MovieController:
    handler = TMDB()
    @staticmethod
    def get_min_movie_info(id):
        data = MovieController.handler.request(f"movie/{id}")
        if data:
            response = {
                "id": data["id"],
                "media_type": "movie",
                "title": data["title"],
                "poster_url": data["poster_path"],
                "year": data["release_date"].split('-')[0]
            }
            return jsonify(response), 200

        return  {}
    
    def get_movie_info(id,uid):
        data = MovieController.handler.request(f"movie/{id}")
        if data:
            data = data
            status = Record.check_media_status(uid=uid,media_type="movie",media_id=id)
            if not status:
                status = "none"
            else:
                status = str(status.status)
            response = {
                "cbfc": "A" if data["adult"] else "U",
                "genre": [str(genre["id"]) for genre in data["genres"]],
                "id": str(data["id"]),
                "imdb_id":data["imdb_id"],
                "media_type": "movie",
                "runtime":data["runtime"] if data["runtime"] else "0",
                "title": data["title"],
                "plot": data["overview"],
                "poster_url": data["poster_path"],
                "release_date": data["release_date"],
                "status": str(status)
            }
            return response

        return  {}
    
    def search_movie(keyword):
        data = MovieController.handler.request(f"search/movie?query={keyword}&include_adult=true").get("results",None)
        if data:
            response = {"results":[]}
            for result in data:
                if result["poster_path"]:
                    response["results"].append({
                        "id": result["id"],
                        "title":result["title"],
                        "media_type": "movie",
                        "poster_url":str(result["poster_path"]),
                        "year": result["release_date"].split('-')[0]
                    })

            return response
        else:
            return {}

