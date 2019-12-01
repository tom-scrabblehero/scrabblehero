import os

from flask import Flask
from werkzeug.utils import import_string

from .models import db


def create_app(environment=None):
    environment = environment or os.environ['FLASK_ENV']
    config = import_string(f"app.config.{environment.capitalize()}Config")

    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    @app.route('/')
    def index():
        return "Hello world!"

    return app
