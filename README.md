
# Generator cards for Anki
## Note
* help to generate cards for ANKI;
* use Longman online dictionary;
* generate cards with field:
    - word (word used for search);
    - sound (sound headline);
    - headline (from Longman);
    - description;
    - thesarusus;
    - example;
    - ref(base word - word witch use first);
    - tags;

# Manual
1Make new words:
1. Set config.py - fill related path and folder.
    1. Add files with new words (books) in folder *./input_data/sources*. Name of file will be used as *source_tag*.
    2. Start *dictionary_book.py*:
        - program find new words in sources;
        - filter them by file WORDS_KNOWN;
        - put in folder WORDS_IN_BOOK; 
2. Generate txt file for ANKI
    4. Start *make_record.py*:
        - program take *WORDS_NEW*;
        - filter by *WORDS_KNOWN*, *WORDS_IN_STUDY*;
        - add all new word in file *FILE_REL_RECORD*
        - add added word in *WORDS_IN_STUDY*;
    
    
