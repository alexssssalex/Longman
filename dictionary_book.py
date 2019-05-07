
FILE_BOOK = '1.txt'

DIR_BOOK = './input_data/book'
OUT_BOOK = './output_data/words_count.txt'
step = 5000
import os

import nltk
from collections import Counter
import spacy
from nltk.corpus import words

WORDS = set(words.words())

def check(token):
    return not token.is_stop and \
           not token.is_punct and \
           token.lemma_.isalpha() and \
           token.lemma_ in WORDS and \
           len(token.lemma_) > 1

nltk.download('words')
nlp = spacy.load('en', disable=['parser', 'ner'])
books = [os.path.join(DIR_BOOK, f) for f in os.listdir(DIR_BOOK) if os.path.isfile(os.path.join(DIR_BOOK, f))]

lem = list()
sss = list()
for book in books:
    f=open(book, encoding='utf-8')
    s = f.read()
    s = s.lower()
    s = s.replace('\r',' ').replace('\n',' ').split()
    s = list(filter(lambda x: all([ord(c) < 128 for c in x]), s))
    sss.extend(s)
    f.close()
chunks = [sss[x:x + step] for x in range(0, len(sss), step)]
print('Number chunks: ', len(chunks))
print('Process chunk #: ')
for i, s in enumerate(chunks):
    s = ' '.join(s)
    if i%20 != 0:
        print(i, end=':')
    else:
        print(i)
    doc = nlp(s)
    lem.extend([token.lemma_ for token in doc if check(token)])
# wor = Counter(lem)
# wor_ = [(v,k) for k,v in wor.items()]
wor = list(set(lem))
wor.sort()
f = open(OUT_BOOK,'w')
for v in wor:
    f.write(str(v)+'\n')
f.close()