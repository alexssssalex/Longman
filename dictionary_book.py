
from config import FILE_KNOWN, DIR_BOOK, OUT_BOOK, step, FILE_ADDED
import os

import nltk
from collections import Counter
import spacy
from nltk.corpus import words

from auxulary.auxilary import made_tag, check, read_arrange

nlp = spacy.load('en', disable=['parser', 'ner'])


books = [os.path.join(DIR_BOOK, f) for f in os.listdir(DIR_BOOK) if os.path.isfile(os.path.join(DIR_BOOK, f))]

lem = dict()        # list lemm
data = dict()       # list words
for book in books:
    tag = made_tag(book)
    data[tag] = list()
    with open(book, encoding='utf-8') as f:
        s = f.read().lower().split()
        s = list(filter(lambda x: all([ord(c) < 128 for c in x]), s))
        data[tag].extend(s)

all_words = read_arrange(FILE_KNOWN)
all_words.update(read_arrange(FILE_ADDED))

for tag in data:
    lem[tag] = list()
    chunks = [data[tag][x:x + step] for x in range(0, len(data[tag]), step)]
    print('Process source: ', tag)
    print('Number chunks:   ', len(chunks))
    print('_process chunk #: ')
    for i, s in enumerate(chunks):
        s = ' '.join(s)
        if i%20 != 0:
            print(i, end=':')
        else:
            print(i)
        doc = nlp(s)
        lem[tag].extend([token.lemma_ for token in doc if check(token, all_words)])
    all_words.update(lem[tag])


with open(OUT_BOOK, 'w') as f:
    for tag in lem:
        wor = Counter(lem[tag])
        wor = sorted([(k, v, tag) for k, v in wor.items()], key=lambda x: x[1], reverse=True)
        for v in wor:
            f.write(str(v[0])+'\n')
