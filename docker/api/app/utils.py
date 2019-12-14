import os
import datetime as dt
import string
import itertools

from yaml import Loader as YamlLoader, load as load_yaml


app_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.abspath(os.path.join(app_dir, '..', 'data'))
scrabble_yml = os.path.join(data_dir, 'scrabble.yml')

scrabble = load_yaml(open(scrabble_yml, 'r').read(), Loader=YamlLoader)


class WordGenerator(object):

    def parse(self, line):
        word, definition = line.split('\t', maxsplit=1)
        return {
            'id': word,
            'definition': definition.strip()
        }

    def readlines(self):
        with open(os.path.join(data_dir, 'words.txt'), 'r') as wf:
            for line in wf.readlines():
                yield line

    def __iter__(self):
        for line in self.readlines():
            yield self.parse(line)
