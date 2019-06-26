# from auxulary.auxilary import read_arrange
from Longman import Longman

from config import WORDS_NEW

option = 1

l = Longman()
with open(WORDS_NEW, mode='r') as f:
    for w in f.readlines():
        w = w.strip()
        if w:
            l.add_record(w)


