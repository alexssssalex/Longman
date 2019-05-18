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
        self.old = self.old_entry()
        for d in [FILE_LOG, FILE_RECORD, FILE_ADDED]:
            f = open(d, mode="w", encoding="utf-8")
            f.close()

    def old_entry(self):
        f = open(FILE_ALL_DATA, 'r')
        old = f.readlines()
        f.close()

        old = list(filter(None, set([x.strip() for x in old])))
        old.sort()

        f = open(FILE_ALL_DATA, 'w')
        f.writelines(map(lambda x: x + '\n', old))
        f.close()
        return set(old)

    def write_new(self, data):
        f = open(FILE_ADDED, mode='a', encoding="utf-8")
        f.write(data + '\n')
        print(data)
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

    def add_record(self, word):
        if word not in self.old_entry():
            res = list()
            res.append(word)
            entry = self.get_entry(word)
            if entry:
                for w in entry.find_all("span", {"class": "ldoceEntry Entry"}):
                    for w1 in w.find_all("span", {"class": "Sense"}):
                        for w2 in w1.find_all("span", {'class': "Crossref"}):
                            for w3 in w2.find_all("a", {'class': "crossRef"}):
                                res.append(w3['href'].split('/')[-1])
                for w in res:
                    self.record(w)
            else:
                self.write_log(str(word) + ' - unknown in Longman\n')


    def record(self, word):
        if word in self.old:
            return None
        res = list()
        headlines = list()
        examples = list()
        tesarusus = list()
        entries = list()
        sounds = list()
        entry = self.get_entry(word)
        if entry is not None:
            word_raw = word

            # <editor-fold desc="Make entries. Delete java">
            for div in entry.find_all("script", {"type": "text/javascript"}):
                div.decompose()
            entries.append(str(entry).replace('\r', '').replace('\n', ''))
            # </editor-fold>

            #find reference
            for w in entry.find_all("span", {"class": "ldoceEntry Entry"}):
                for w1 in w.find_all("span", {"class": "Sense"}):
                    for w2 in w1.find_all("span", {'class':"Crossref"}):
                        for w3 in w2.find_all("a", {'class': "crossRef"}):
                            res.append(w3['href'].split('/')[-1])

            word = entry.find("h1", {"class": "pagetitle"}).text

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
            self.write_new(word_raw)
            self.old.add(word_raw)
        return res

f = open(FILE_ALL_DATA, 'r')
old = f.readlines()
f.close()

f = open(FILE_INPUT, 'r')
new = f.readlines()
new = list(filter(None, set([x.strip() for x in new])))
f.close()

old = list(filter(None, set([x.strip() for x in old])))
old.sort()

# f = open(FILE_ALL_DATA, 'w')
# f.writelines(map(lambda x: x +'\n', old))
# f.close()

d = Dict()
for w in new:
    d.add_record(w)

