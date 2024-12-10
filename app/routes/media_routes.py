from flask import Blueprint, request
from app.controllers import MovieController,SeriesController, AnimeController
from app.utils import cache_response

media_blueprint = Blueprint('child','media', __name__)


# MOVIE ROUTES

@media_blueprint.route('/min/movie/<int:movie_id>')
@cache_response()
def get_min_movie_info(movie_id):
    return MovieController.get_min_movie_info(movie_id)

@media_blueprint.route('/movie/<int:movie_id>')
def get_movie_info(movie_id):
    uid = request.headers.get('uid')
    return MovieController.get_movie_info(movie_id,uid)

@media_blueprint.route('/movie/search')
def search_movie():
    query = request.args.get("q")
    return MovieController.search_movie(query)


# SERIES ROUTES
@media_blueprint.route('/min/tvseries/<int:movie_id>')
@cache_response()
def get_min_series_info(movie_id):
    return SeriesController.get_min_series_info(movie_id)

@media_blueprint.route('/tvseries/<int:movie_id>')
def get_series_info(movie_id):
    uid = request.headers.get('uid')
    return SeriesController.get_series_info(movie_id,uid)

@media_blueprint.route('/tvseries/search')
def search_series():
    query = request.args.get("q")
    return SeriesController.search_series(query)


# ANIME ROUTES

@media_blueprint.route('/anime/search')
def search_anime():
    query = request.args.get("q")
    return AnimeController.search_anime(query)

@media_blueprint.route('/min/anime/<int:movie_id>')
@cache_response()
def get_min_anime_info(movie_id):
    return AnimeController.get_min_anime_info(movie_id)

@media_blueprint.route('/anime/<int:movie_id>')
def get_anime_info(movie_id):
    uid = request.headers.get('uid')
    return AnimeController.get_anime_info(movie_id,uid)

#Manga Routes

@media_blueprint.route('/manga/<int:manga_id>')
def get_manga_info(manga_id):
    pass

@media_blueprint.route('/book/<int:book_id>')
def get_book_info(book_id):
    pass

@media_blueprint.route('/game/<int:game_id>')
def get_game_info(game_id):
    pass

@media_blueprint.route('/lightnovel/<int:lightnovel_id>')
def get_lightnovel_info(lightnovel_id):
    pass