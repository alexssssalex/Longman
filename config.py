import os

step = 10000        #NUMBER WORD TO SPLIT PROCESS

FOLDER_DATA = 'd:/cloud/YandexDisk/YandexDisk/ProgramPython/Longman/'

FOLDER_REL_BOOK = os.path.join(FOLDER_DATA, 'input_data/sources')           # dir with files book to find new words
FOLDER_REL_MEDIA = os.path.join(FOLDER_DATA, 'output_data/media/')

WORDS_KNOWN = os.path.join(FOLDER_DATA, 'data_base/words_known.txt')  # known words
WORDS_NEW = os.path.join(FOLDER_DATA, 'input_data/words_new.txt')    # file new word to add
WORDS_IN_BOOK = os.path.join(FOLDER_DATA, 'input_data/words_book.txt')    # file new word from book
WORDS_IN_STUDY = os.path.join(FOLDER_DATA, 'data_base/words_in_study.txt')

FILE_REL_LOG = os.path.join(FOLDER_DATA, 'output_data/log.txt')
FILE_REL_RECORD = os.path.join(FOLDER_DATA, 'output_data/record.txt')

DELIMETER  = '|'
