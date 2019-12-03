import os
import datetime as dt
import string
import itertools


app_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.abspath(os.path.join(app_dir, '..', 'data'))

letter_points = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 4,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10
}


class WordGenerator(object):
    def valid_line(self, line):
        if line.startswith('  '):
            return False
        else:
            return True

    def valid_word(self, word):
        return word.isalnum() and not any(c.isdigit() for c in word)

    def score_word(self, word):
        return sum(letter_points.get(c) for c in word)

    def iter_file_paths(self):
        wordnet_dir = os.path.join(data_dir, 'wordnet')
        for fn in os.listdir(wordnet_dir):
            yield os.path.join(wordnet_dir, fn)

    def iter_lines(self):
        for path in self.iter_file_paths():
            with open(path, 'r') as f:
                for line in f.readlines():
                    yield line

    def iter_words(self):
        for line in self.iter_lines():
            if self.valid_line(line):
                word = line.split()[0]
                if self.valid_word(word):
                    yield word

    def generate_words(self, as_tuples=False):
        now = dt.datetime.now()
        unique_words = list(sorted(set(self.iter_words())))
        result = [
            {
                "value": w,
                "score": self.score_word(w),
                "created_at": now,
                "updated_at": now
            } for w in unique_words
        ]

        if as_tuples:
            return [(w['created_at'], w['updated_at'], w['value'], w['score']) for w in result]
        else:
            return result

    def generate_character_pairs(self):
        pairs = [a + b for a,b in itertools.product(string.ascii_lowercase, string.ascii_lowercase)]
        return list(zip(pairs[:-1], pairs[1:]))
