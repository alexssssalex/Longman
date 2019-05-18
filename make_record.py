# from auxulary.auxilary import read_arrange
from Longman import Longman

from config import WORDS_NEW

l = Longman()
with open(WORDS_NEW, mode='r') as f:
    for w in f.readlines():
        l.add_record(w.strip())


