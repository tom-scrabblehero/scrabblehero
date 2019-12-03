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
    recommendations: 'RelatedWord'

    value = db.Column(db.String(), primary_key=True)
    score = db.Column(db.Integer(), nullable=False)

    recommendations = db.relationship("RelatedWord", lazy="joined", primaryjoin="Word.value==RelatedWord.word")


@dataclass
class RelatedWord(db.Model, TimestampMixin):
    related: str
    score_difference: int
    distance: float
    recommendation: float

    word = db.Column(db.String(), db.ForeignKey('word.value'), primary_key=True, nullable=False)
    related = db.Column(db.String(), primary_key=True)
    score_difference = db.Column(db.Integer(), nullable=False, index=True)
    distance = db.Column(db.Float(), nullable=False, index=True)
    recommendation = db.Column(db.Float(), nullable=True)

    def __repr__(self):
        return f"<Recommendation {self.related}: {self.recommendation}>"
