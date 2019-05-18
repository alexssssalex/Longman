#script make list of word in book

from config import FOLDER_REL_BOOK, WORDS_IN_BOOK, step
import os

from collections import Counter
import spacy

from auxulary.auxilary import made_tag, check, read_arrange

nlp = spacy.load('en', disable=['parser', 'ner'])

books = [os.path.join(FOLDER_REL_BOOK, f) for f in os.listdir(FOLDER_REL_BOOK) if os.path.isfile(os.path.join(FOLDER_REL_BOOK, f))]

lem = dict()        # list lemm
data = dict()       # dictionary with books ( input data)
words = set()       # words
# <editor-fold desc="Read books as dictionary and remove non unicode">
for book in books:
    tag = made_tag(book)
    data[tag] = list()
    with open(book, encoding='utf-8') as f:
        s = f.read().lower().split()
        s = list(filter(lambda x: all([ord(c) < 128 for c in x]), s))
        data[tag].extend(s)
# </editor-fold>

# <editor-fold desc="Make list words from book">
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
        lem[tag].extend([token.lemma_ for token in doc if check(token)])
# </editor-fold>


# <editor-fold desc="Write book in frequency order">
with open(WORDS_IN_BOOK, 'w') as f:
    for tag in lem:
        wor = Counter(lem[tag])
        wor = sorted([(k, v, tag) for k, v in wor.items()], key=lambda x: x[1], reverse=True)
        for v in wor:
            f.write(str(v[0])+'\n')
# </editor-fold>
