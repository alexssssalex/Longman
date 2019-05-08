
# Project to generate cards for program Anki
This program help to generate cards for ANKI base on Longman dictionary

# Alghoritm work
1. Add files with new words in folder *./input_data/sources*. Name of file will be used as *source_tag*.
2. Start *dictionary_book.py*:
	- program find new words in sources;
	- filter them by file *./data_base/words_known.txt*;
	- put in folder *./input_data/words_new.txt*; 
3. Check  manually *./input_data/words/words_new.txt* and copy if need known word in *./data_base/words_known.txt*;
4. Start *sss.py*:
	- program take *./input_data/words/words_new.txt*;
	- filter by *./data_base/words_known.txt*;
	- filter by *./data_base/words_in_study.txt*;
	- add all new word in file *./output_data/record.txt*
	- add added word in *./data_base/words_in_study.txt*;


