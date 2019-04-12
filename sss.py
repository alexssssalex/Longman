from bs4 import BeautifulSoup
import requests
import wget
import os
from urllib.parse import urlparse
import re

FOLDER_MEDIA = './media/'
FILE_LOG = 'log.txt'
FILE_INPUT = 'word_input.txt'
FILE_ADDED = 'word_added.txt'
FILE_RECORD = 'record.txt'

FILE_ALL_DATA = './data/words.txt'
DELIMETER  = '|'


class Dict:

    def __init__(self):
        """
        file - name file for records
        """
        for d in [FILE_LOG, FILE_RECORD]:
            f = open(d, mode="w", encoding="utf-8")
            f.close()

    def write_log(self, data):
        f = open(FILE_LOG, mode='a', encoding="utf-8")
        f.write(data)
        print(data)
        f.close()

    def write_rec(self, data):
        f = open(FILE_RECORD, mode='a', encoding="utf-8")
        f.write(data)
        f.close()


    def get_mp3(self, url: str) -> str:
        """
        url - adress file
        return name file
        """
        nm = os.path.basename(urlparse(url).path)
        nm_path = FOLDER_MEDIA+nm
        if not os.path.isfile(nm_path):
            try:
                wget.download(url, nm_path)
            except:
                self.write_log(nm + 'is not downloaded\n')
                nm = ''
        return nm

    def get_entry(self, word: str) -> BeautifulSoup:
        url = 'https://www.ldoceonline.com/dictionary/'+word
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/41.0.2272.0 Safari/537.36'}
        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.content, "html.parser")
        return soup.find("div", {"class": "entry_content"})

    def get_str_entry(self, data):
        rec = '<span class="ldoceEntry Entry">'
        for d in data:
            rec += str(d)
        rec += '</span>'
        return rec.replace(DELIMETER,' ')

    def get_str_sound(self, data):
        rec = ''
        for d in data:
            rec +='[sound:' + d + ']'
        return rec


    def record(self, word):
        headlines = list()
        examples = list()
        tesarusus = list()
        entries = list()
        sounds = list()
        entry = self.get_entry(word)
        res = False
        if entry is not None:

            # <editor-fold desc="Make entries. Delete java">
            for div in entry.find_all("script", {"type": "text/javascript"}):
                div.decompose()
            entries.append(str(entry).replace('\r', '').replace('\n', ''))
            # </editor-fold>

            word = entry.find("h1", {"class": "pagetitle"}).text
            print(word)

            # <editor-fold desc="Thesarusus">
            for div in entry.find_all("span", {"class": "ThesBox"}):
                tesarusus.append(str(div).replace('\r', '').replace('\n', ''))
            # </editor-fold>

            # <editor-fold desc="Example">
            for div in entry.find_all("span", {"class": "EXAMPLE"}):
                examples.append(str(div).replace('\r', '').replace('\n', ''))
            # </editor-fold>

            # <editor-fold desc="Headlines and Sounds">
            for div in entry.find_all("span", {"class":re.compile(r'(frequent Head|Head)')}):
                for sound in div.find_all("span", {"data-src-mp3": True}):
                    nm = self.get_mp3(sound.attrs['data-src-mp3'])
                    if nm:
                        sounds.append(nm)
                for x in ["HWT","HYPHENATION", "HOMNUM", 'tooltip LEVEL', "FREQ"]:
                    while div.find("span", {"class": x}):
                        y = div.find("span", {"class": x})
                        if y is not None:
                            y.decompose()
                headlines.append(str(div).replace('\r', '').replace('\n', '')+'<br>')
            # </editor-fold>
            rec = word + DELIMETER + self.get_str_sound(sounds)
            for x in [headlines, entries, tesarusus, examples]:
                rec = rec + DELIMETER +self.get_str_entry(x)
            rec += '\n'
            self.write_rec(rec)
            res = True
        else:
            res = False
        return res

f = open(FILE_ALL_DATA, 'r')
old = f.readlines()
f.close()

f = open(FILE_INPUT, 'r')
new = f.readlines()
f.close()

old = list(filter(None, set([x.strip() for x in old])))
new = [y for y in list(filter(None, set([x.strip() for x in new]))) if y not in old]
old.sort()
new.sort()

f = open(FILE_ALL_DATA, 'w')
f.writelines(map(lambda x: x +'\n', old))
f.close()

f = open(FILE_ADDED, 'w')
d = Dict()
for w in new:
    print('\n'+w)
    if not d.record(w):
        d.write_log(w + ' - unknown in Longman\n')
    else:
        print(w+'-done')
        f.write(w+'\n')
f.close()

