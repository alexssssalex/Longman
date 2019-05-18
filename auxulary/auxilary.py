import nltk
import os

from nltk.corpus import words
nltk.download('words')
WORDS = set(words.words())


def check(token):
    """
    - take token;
    - check if we need add this token to words serch;
    - return True if it needs add

    """
    return not token.is_stop and \
        not token.is_punct and \
        token.lemma_.isalpha() and \
        token.lemma_ in WORDS and \
        len(token.lemma_) > 1


def made_tag(path):
    """
    made tag from path:
    -take base name;
    -remove all after last '.'
    -replace all non alphabet on '_'
    """
    return ''.join(map(lambda x: x if x.isalpha() else '_', os.path.basename(path).rsplit('.', 1)[0]))


def read_arrange(path: str) -> list:
    """
    - read file by path;
    - filter empty lines;
    - made unique list;
    - return unique list of words (in order in input file);
    - arrange list set and save word in the same file in alphabet order;
    """
    word_set = set()
    word_new = list()
    with open(path, 'r') as f:
        data = [w.split(':')[0].strip() for w in f.readlines()]
    data = list(filter(lambda x: len(x) > 0, data))
    for w in data:
        if w not in word_set:
            word_new.append(w)
            word_set.add([w])
    with open(path, 'w') as f:
        word_new_ = list(word_set)
        word_new_.sort()
        f.writelines([w+'\n' for w in word_new_])
    return word_new

