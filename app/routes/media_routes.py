from flask import Blueprint
from app.controllers import MovieController
from app.utils import cache_response

media_blueprint = Blueprint('media', __name__)

@media_blueprint.route('/info/movie/<string:movie_id>')
@cache_response()
def get_movie_info(movie_id):
    return MovieController.get_movie_info(movie_id)

@media_blueprint.route('/info/tvseries/<int:tvseries_id>')
def get_tvseries_info(tvseries_id):
    pass

@media_blueprint.route('/info/anime/<int:anime_id>')
def get_anime_info(anime_id):
    pass

@media_blueprint.route('/info/manga/<int:manga_id>')
def get_manga_info(manga_id):
    pass

@media_blueprint.route('/info/book/<int:book_id>')
def get_book_info(book_id):
    pass

@media_blueprint.route('/info/game/<int:game_id>')
def get_game_info(game_id):
    pass

@media_blueprint.route('/info/lightnovel/<int:lightnovel_id>')
def get_lightnovel_info(lightnovel_id):
    pass