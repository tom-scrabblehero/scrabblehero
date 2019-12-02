import os


class WordGenerator(object):
    def valid_line(self, line):
        if line.startswith('  '):
            return False
        else:
            return True

    def valid_word(self, word):
        return word.isalnum() and not any(c.isdigit() for c in word)

    def iter_file_paths(self):
        app_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.abspath(os.path.join(app_dir, '..', 'data'))
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

    def generate_words(self):
        unique_words = list(sorted(set(self.iter_words())))
        return [{"value": w} for w in unique_words]
