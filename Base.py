from config import WORDS_IN_STUDY, WORDS_KNOWN

def read_arrange(path: str) -> set:
    """
    - read file by path;
    - filter empty lines;
    - made unique list;
    - arrange list set and save word in the same file in alphabet order;
    """
    with open(path, 'r') as f:
        data = [w.split(':')[0].strip() for w in f.readlines()]
    word_set = set(filter(lambda x: len(x) > 0, data))
    with open(path, 'w') as f:
        words = list(word_set)
        words.sort()
        f.writelines([w+'\n' for w in words])
    return word_set

class Base:

    def __init__(self):
        self.words = read_arrange(WORDS_KNOWN)
        self.words.update(read_arrange(WORDS_IN_STUDY))

    def __contains__(self, item):
        return item in self.words

    def update(self, item):
        if item not in self.words:
            with open(WORDS_IN_STUDY, 'a') as f:
                self.words.update([item])
                f.write(item+'\n')

if __name__=='__main__':
    print('I am here')
    b = Base()
    print(b.words)
    x = 'dfg'
    print(x in b)
    b.update(x)
    print(x in b)
    print(b.words)

