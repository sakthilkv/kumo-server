import json

from flask import jsonify
from app.core import TMDbAPIHandler as TMDB

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
    def get_movie_info(id):
        data = MovieController.handler.request(f"movie/{id}").get("movie_results",None)
        if data:
            data = data[0]
            response = {
                "id": data["id"],
                "media_type": "movie",
                "title": data["title"],
                "plot": data["overview"],
                "poster_url": data["poster_path"],
                "release_date": data["release_date"]
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

