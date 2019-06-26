import os

step = 10000        #NUMBER WORD TO SPLIT PROCESS

FOLDER_DATA = 'd:/cloud/YandexDisk/YandexDisk/ProgramPython/Longman/'       # reference folder with data

FOLDER_REL_BOOK = os.path.join(FOLDER_DATA, 'input_data/sources')           # input folder with sources(book) (to find new words)

WORDS_KNOWN = os.path.join(FOLDER_DATA, 'data_base/words_known.txt')        # words known (filter this word will not add)
WORDS_NEW = os.path.join(FOLDER_DATA, 'input_data/words_new.txt')           # words new (will be used to add)
WORDS_IN_BOOK = os.path.join(FOLDER_DATA, 'input_data/words_new.txt')      # words new from book
WORDS_IN_STUDY = os.path.join(FOLDER_DATA, 'data_base/words_in_study.txt')  # words in study (filter update )

FILE_REL_LOG = os.path.join(FOLDER_DATA, 'output_data/log.txt')             # output log file
FILE_REL_RECORD = os.path.join(FOLDER_DATA, 'output_data/record.txt')       # output txt file for ANKI
FOLDER_REL_MEDIA = os.path.join(FOLDER_DATA, 'output_data/media/')          # output media folder files

DELIMETER  = '|'
