import os
from flask import Flask, send_from_directory
import logging

from flask_cors import CORS

from config import Config
from extension import db

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def register_extensions(app):
    with app.app_context():
        db.init_app(app)
    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)

    @app.route('/public/<path:filename>')
    def public_files(filename):
        return send_from_directory(os.path.join(app.root_path, 'public'), filename)
    
    return app

app = create_app(Config)

if __name__ == "__main__":
    app.run(debug = True)