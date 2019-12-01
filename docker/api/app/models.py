import datetime as dt

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, default=dt.datetime.now)
    updated_at = db.Column(db.DateTime, default=dt.datetime.now, onupdate=dt.datetime.now)

class Word(db.Model):
    id = db.Column(db.String(), primary_key=True)
