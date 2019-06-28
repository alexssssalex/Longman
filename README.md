
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
1. Set config.py:

1. Add files with new words in folder *./input_data/sources*. Name of file will be used as *source_tag*.
2. Start *dictionary_book.py*:
	- program find new words in sources;
	- filter them by file *./data_base/words_known.txt*;
	- put in folder *./input_data/words_new.txt*; 
3. Check  manually *./input_data/words/words_new.txt* and copy if need known word in *./data_base/words_known.txt*;
4. Start *make_record.py*:
	- program take *./input_data/words/words_new.txt*;
	- filter by *./data_base/words_known.txt*;
	- filter by *./data_base/words_in_study.txt*;
	- add all new word in file *./output_data/record.txt*
	- add added word in *./data_base/words_in_study.txt*;

# Instalation note

* go to conda envs in **as admine **
* activate envs
* run cmd: 
    * python.exe -m spacy download en


