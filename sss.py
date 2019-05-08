
import os
from auxulary.auxilary import read_arrange
from Longman import Longman

FOLDER_MEDIA = './media/'


FILE_LOG = './output_data/log.txt'
FILE_INPUT = './input_data/words_new.txt'
FILE_ADDED = './data_base/words_in_study.txt'
FILE_RECORD = './output_data/record.txt'

FILE_ALL_DATA = './data_base/words_known.txt'


old = read_arrange(FILE_ALL_DATA)
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

