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
    score: int

    value = db.Column(db.String(), primary_key=True)
    score = db.Column(db.Integer(), nullable=False)


@dataclass
class RelatedWord(db.Model, TimestampMixin):
    word = db.Column(db.String(), db.ForeignKey('word.value'), primary_key=True, nullable=False)
    related = db.Column(db.String(), primary_key=True)
    score_difference = db.Column(db.Integer(), nullable=False, index=True)
    distance = db.Column(db.Float(), nullable=False, index=True)
    recommendation = db.Column(db.Float(), nullable=True)
