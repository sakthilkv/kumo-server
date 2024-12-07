import json
from app.core import TMDbAPIHandler as TMDB

class SeriesController:
    handler = TMDB()
    @staticmethod
    def get_min_movie_info(id):
        data = SeriesController.handler.request(f"find/{id}?external_source=imdb_id").get("movie_results",None)
        if data:
            data = data[0]
            response = {
                "id": data["id"],
                "media_type": "series",
                "title": data["title"],
                "poster_url": data["poster_path"],
                "year": data["release_date"].split('-')[0]
            }
            return response

        return  {}
    def get_movie_info(id):
        data = SeriesController.handler.request(f"find/{id}?external_source=imdb_id").get("movie_results",None)
        if data:
            data = data[0]
            response = {
                "id": data["id"],
                "media_type": "series",
                "title": data["title"],
                "plot": data["overview"],
                "poster_url": data["poster_path"],
                "release_date": data["release_date"]
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

