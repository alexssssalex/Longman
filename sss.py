import os
from auxulary.auxilary import read_arrange
from Longman import Longman

from config import FOLDER_MEDIA, FILE_LOG, FILE_INPUT, FILE_ADDED, FILE_RECORD, FILE_ALL_DATA


old = read_arrange(FILE_ALL_DATA)
old.update(read_arrange(FILE_ADDED))
new = read_arrange(FILE_INPUT)
new = new - old

f = open(FILE_ADDED, 'w')
d = Longman(FILE_LOG, FILE_RECORD, FOLDER_MEDIA)
for w in new:
    print('\n'+w)
    if not d.record(w):
        d.write_log(w + ' - unknown in Longman\n')
    else:
        print(w+'-done')
        f.write(w+'\n')
f.close()

