import nltk
import os

from nltk.corpus import words
nltk.download('words')
WORDS = set(words.words())


def check(token, all_word):
    """
    - take token;
    - check if we need add this token to words serch;
    - return True if it needs add

    """
    return not token.is_stop and \
        not token.is_punct and \
        token.lemma_.isalpha() and \
        token.lemma_ in WORDS and \
        len(token.lemma_) > 1 and \
        token.lemma_ not in all_word


def made_tag(path):
    """
    made tag from path:
    -take base name;
    -remove all after last '.'
    -replace all non alphabet on '_'
    """
    return ''.join(map(lambda x: x if x.isalpha() else '_', os.path.basename(path).rsplit('.', 1)[0]))


def read_arrange(path):
    """
    - read file by path;
    - arrange word in file;
    - filter empty lines;
    - made set of word;
    - arrange set and save word in the same file;
    - return set;
    """
    with open(path, 'r') as f:
        word = [w.split(':')[0].strip() for w in f.readlines()]
    word = set(filter(lambda x: len(x) > 0, word))
    with open(path, 'w') as f:
        words_ = list(word)
        words_.sort()
        f.writelines([w+'\n' for w in words_])
    return word

