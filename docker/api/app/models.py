import datetime as dt
from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, default=dt.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=dt.datetime.now, onupdate=dt.datetime.now, nullable=False)


@dataclass
class Word(db.Model, TimestampMixin):
    value: str

    value = db.Column(db.String(), primary_key=True)
