import json
from app.core import TMDbAPIHandler as TMDB

class SeriesController:
    handler = TMDB()
    @staticmethod
    def get_min_series_info(id):
        data = SeriesController.handler.request(f"tv/{id}")
        if data:
            response = {
                "id": data["id"],
                "media_type": "tvseries",
                "title": data["name"],
                "poster_url": data["poster_path"],
                "year": data["first_air_date"].split('-')[0]
            }
            return response

        return  {}
    def get_series_info(id):
        data = SeriesController.handler.request(f"tv/{id}")
        if data:
            if  not ("16" in [str(genre["id"]) for genre in data["genres"]] and any(country in ["JP", "CN", "KR"] for country in data["origin_country"])):
                response = {
                    "cbfc": "A" if data["adult"] else "U",
                    "genre": [str(genre["id"]) for genre in data["genres"]],
                    "id": str(data["id"]),
                    "media_type": "movie",
                    "runtime":data["last_episode_to_air"]["runtime"] if data["last_episode_to_air"]["runtime"] else "0",
                    "title": data["name"],
                    "plot": data["overview"],
                    "poster_url": data["poster_path"],
                    "release_date": data["first_air_date"]
                }
                return response

        return  {}
    
    def search_series(keyword):
        data = SeriesController.handler.request(f"search/tv?query={keyword}&include_adult=true").get("results",None)
        if data:
            response = {"results":[]}
            for result in data:
                if result["poster_path"] and  not (16 in result["genre_ids"] and any(country in ["JP", "CN", "KR"] for country in result["origin_country"])):
                    response["results"].append({
                        "id": result["id"],
                        "title":result["name"],
                        "media_type": "tvseries",
                        "poster_url":str(result["poster_path"]),
                        "year": result["first_air_date"].split('-')[0]
                    })
            return response
        else:
            return {}

