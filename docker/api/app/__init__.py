import os

from flask import Flask
from werkzeug.utils import import_string


def create_app(environment=None):
    environment = environment or os.environ['FLASK_ENV']
    config = import_string(f"app.config.{environment.capitalize()}Config")

    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/')
    def index():
        return "Hello world!"

    return app
