import os
from flask import Blueprint, Flask, send_from_directory
import logging
from sqlalchemy import text
from flask_cors import CORS

from config import Config
from extension import db
from app.routes import user_blueprint, media_blueprint

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def register_extensions(app):
    with app.app_context():
        db.init_app(app)
    CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://localhost:8000","http://192.168.0.104:5173"]}})
    api_blueprint = Blueprint('parent','api', __name__)
    api_blueprint.register_blueprint(user_blueprint,url_prefix = "/user")
    api_blueprint.register_blueprint(media_blueprint,url_prefix = "/media")
    app.register_blueprint(api_blueprint,url_prefix = "/api")

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)

    @app.route('/public/<path:filename>')
    def public_files(filename):
        return send_from_directory(os.path.join(app.root_path, 'public'), filename)
    
    return app

  

app = create_app(Config)

with app.app_context():
    try:
        result = db.session.execute(text('SELECT 1'))
        logging.info(f"Database connection successful!")
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")

if __name__ == "__main__":
    app.run(debug = True)