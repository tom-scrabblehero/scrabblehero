import datetime as dt
from operator import mul
from dataclasses import dataclass, asdict
from collections import OrderedDict
from functools import reduce
from collections import Counter
from itertools import combinations

from flask_sqlalchemy import SQLAlchemy

from .utils import scrabble


db = SQLAlchemy()


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, default=dt.datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=dt.datetime.now, onupdate=dt.datetime.now, nullable=False)


# TODO: add lengths to the database, and pull recommended words via subset anagram hashes
@dataclass
class Word(db.Model, TimestampMixin):
    created_at: dt.datetime
    updated_at: dt.datetime
    id: str
    score: int
    anagram_hash: int
    frequency: float
    length: int

    id = db.Column(db.String(), primary_key=True)
    score = db.Column(db.Integer(), nullable=False)
    anagram_hash = db.Column(db.String(), nullable=False, index=True)
    frequency = db.Column(db.Float(), nullable=False)
    length = db.Column(db.Integer(), nullable=False, index=True)

    @classmethod
    def ordered_columns(klass):
        return sorted(c.name for c in Word.__table__.columns)

    def __init__(self, id, **kwargs):
        kwargs['id'] = id
        super().__init__(**kwargs)
        # These are included to help the seeding function
        self.updated_at = self.updated_at or dt.datetime.now()
        self.created_at = self.created_at or self.updated_at
        self.score = self.score or self.calculate_score()
        self.anagram_hash = self.anagram_hash or self.calculate_anagram_hash()
        self.frequency = self.frequency or self.calculate_frequency()
        self.length = self.length or self.calculate_length()

    def __eq__(self, other):
        return self.anagram_hash == other.anagram_hash

    def __add__(self, other):
        return Word(id=self.id + other.id)

    def __sub__(self, other):
        c1, c2 = Counter(self.id), Counter(other.id)
        letters = ''.join((c1 - c2).elements())
        return Word(id=letters)

    def __repr__(self):
        return self.id

    def __len__(self):
        return len(self.id)

    def __iter__(self):
        for char in self.id:
            yield char

    def calculate_length(self):
        return len(self)

    def calculate_score(self):
        return sum(scrabble['scores'].get(a, 0) for a in self.id)

    def calculate_anagram_hash(self):
        character_hashes = (scrabble['hashes'].get(c, 1) for c in self.id)
        return str(reduce(mul, character_hashes, 1))

    def calculate_frequency(self):
        return 0

    def subsets(self):
        "All unique subsets of the word"
        for n in range(1, len(self) + 1):
            for v in combinations(self.id, n):
                yield Word(id=''.join(v))

    def recommendations(self):
        hashes = [w.anagram_hash for w in self.subsets()]
        return Word.query.filter(Word.anagram_hash.in_(hashes)).order_by(Word.length.desc()).all()

    def ordered_data(self):
        data = asdict(self)
        d = {k: data[k] for k in self.__class__.ordered_columns()}
        return OrderedDict(sorted(d.items()))
