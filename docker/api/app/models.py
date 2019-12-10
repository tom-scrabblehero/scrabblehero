import datetime as dt
from operator import mul
from dataclasses import dataclass, asdict
from collections import OrderedDict
from functools import reduce

from flask_sqlalchemy import SQLAlchemy

from .utils import scrabble


db = SQLAlchemy()


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, default=dt.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=dt.datetime.now, onupdate=dt.datetime.now, nullable=False)


@dataclass
class Word(db.Model, TimestampMixin):
    created_at: dt.datetime
    updated_at: dt.datetime
    id: str
    score: int
    anagram_hash: int
    frequency: float

    id = db.Column(db.String(), primary_key=True)
    score = db.Column(db.Integer(), nullable=False)
    anagram_hash = db.Column(db.BigInteger(), nullable=False)
    frequency = db.Column(db.Float(), nullable=False)

    @classmethod
    def ordered_columns(klass):
        return sorted(klass.__dataclass_fields__.keys())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # These are included to help the seeding function
        self.updated_at = self.updated_at or dt.datetime.now()
        self.created_at = self.created_at or self.updated_at
        self.score = self.score or self.calculate_score()
        self.anagram_hash = self.anagram_hash or self.calculate_anagram_hash()
        self.frequency = self.frequency or self.calculate_frequency()

    def calculate_score(self):
        return sum(scrabble['scores'].get(a, 0) for a in self.id)

    def calculate_anagram_hash(self):
        character_hashes = (scrabble['hashes'].get(c, 1) for c in self.id)
        return reduce(mul, character_hashes, 1)

    def calculate_frequency(self):
        frequency = 1
        letters = scrabble['frequencies'].copy()
        total_letters = sum(x - 2 for x in letters.values())  # minus 2 because of the blanks
        for position, char in enumerate(self.id):
            bag_size = total_letters - position
            appearances = letters[char]
            if appearances > 0:
                letters[char] -= 1
            frequency *= (appearances / bag_size)
        return frequency

    def ordered_data(self):
        return OrderedDict(sorted(asdict(self).items()))
