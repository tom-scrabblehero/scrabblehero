#!/usr/local/bin/python3

"""
Constructs a sitemap from the data in /data/words.txt. Require python3.6+
"""

import os
import sh
import math


sitemap_dir = 'data/sitemap'
sitemap_words_dir = 'data/sitemap/words'
url_string = 'https://www.scrabblehero.com/words/{word}\n'
sitemap_string = sitemap_dir + '/words/{sitemap_number}.txt'

sh.rm('-r', '-f', sitemap_dir)
os.makedirs(sitemap_words_dir, exist_ok=True)

words = open('data/words.txt', 'r').readlines()
sitemap_fh = open(sitemap_string.format(sitemap_number=0), 'w')
for n, word in enumerate(words):
    word = word.strip()
    sitemap_number = math.floor(n / 50000)
    sitemap_filename = sitemap_string.format(sitemap_number=sitemap_number)
    if not os.path.exists(sitemap_filename):
        sitemap_fh.close()
        print(f"Finished writing {sitemap_filename}")
        sitemap_fh = open(sitemap_filename, 'w')
    fword = url_string.format(word=word)
    sitemap_fh.write(fword)
    print(f"Updated {sitemap_filename} with {fword}", end='')
