import json
from app.core import TMDbAPIHandler as TMDB

class MovieController:
    handler = TMDB()
    @staticmethod
    def get_movie_info(id):
        data = MovieController.handler.request(f"find/{id}?external_source=imdb_id")
        if data:
            data = data.get("movie_results",None)[0]
            response = {
                "id": id,
                "media_type": "movie",
                "title": data["original_title"],
                "plot": data["overview"],
                "poster_url": data["poster_path"],
                "year": data["release_date"].split('-')[0]
            }
            return response

        return  {
    "id": "tt17526714",
    "media_type": "movie",
    "plot": "A fading celebrity decides to use a black market drug, a cell-replicating substance that temporarily creates a younger, better version of herself.",
    "poster_url": "/lqoMzCcZYEFK729d6qzt349fB4o.jpg",
    "title": "The Substance",
    "year": "2024"
}