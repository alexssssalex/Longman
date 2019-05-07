
FILE_BOOK = '1.txt'
import nltk
from collections import Counter
import spacy
from nltk.corpus import words

def check(token):
    return not token.is_stop and \
           not token.is_punct and \
           token.lemma_.isalpha() and \
           token.lemma_ in words_dict and \
           len(token.lemma_) > 1


words_dict = set(words.words())
nlp = spacy.load('en', disable=['parser', 'ner'])

nltk.download('words')
f=open(FILE_BOOK)
s = ' '.join(f.read().lower().replace('\r',' ').replace('\n',' ').split())
f.close()
doc = nlp(s)
lem = [token.lemma_ for token in doc if check(token)]
wor = Counter(lem)
z = [(v,k) for k,v in wor.items()]
z.sort(reverse=True)
f = open('2.txt','w')
for v in z:
    f.write(str(v)+'\n')
f.close()