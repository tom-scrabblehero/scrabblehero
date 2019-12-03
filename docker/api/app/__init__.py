import os
import logging

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.utils import import_string

from .models import db, Word
from .cli import seed
from .resources import api


migrate = Migrate(db)


def shell_context():
    return {
        'db': db,
        'Word': Word
    }


def create_app(environment=None):
    environment = environment or os.environ['FLASK_ENV']
    config = import_string(f"app.config.{environment.capitalize()}Config")

    gunicorn_logger = logging.getLogger("gunicorn.error")
    app = Flask(__name__)
    app.config.from_object(config)

    if not app.debug:
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    app.shell_context_processor(shell_context)
    app.cli.add_command(seed)

    api.init_app(app)

    return app
