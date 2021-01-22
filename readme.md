# Words in words

"We put the _laughter_ in _slaughter_"

A quick and dirty script to get all instances of words that appear inside other words. The whole lot is maybe quicker to navigate in [this Google spreadsheet](https://j.mp/2McKenp).

## Notes

All of the code that I used to make the list is in the [python_fun_all_the_scripts](/python_fun_all_the_scripts) folder.

```words_alpha.txt``` is from https://github.com/dwyl/english-words


I haven't looked at the code for a while, I threw it together fairly quickly. But the original runs as an ipython notebook, using tinydb to collate a database.

v0.3 of Python code:

install dependencies:
```python
! pip install tinydb
```

the code:
```python

from tinydb import TinyDB, Query
db = TinyDB('db.json')
wordlist = 'words_alpha.txt'

# uncomment this if you want to start afresh
# db.drop_tables()


def updateShort(short, long):
    if (db.get(q.word == short) == None):
        db.insert({'word':short,'in':[long],'contains':[]})
    else:
        in_ = db.get(q.word == short)['in']
        in_.append(long) if long not in in_ else in_
        db.upsert({'word':short,'in':in_},q.word==short)

def updateLong(short, long):
    if (db.get(q.word == long) == None):
        db.insert({'word':long,'in':[],'contains':[short]})
    else:
        contains_ = db.get(q.word == long)['contains']
        contains_.append(short) if short not in contains_ else contains_
        db.upsert({'word':long,'contains':contains_},q.word==long)

with open(wordlist,'r') as a:
    for short in a:
        short = short.rstrip("\r\n")
        with open(wordlist,'r') as b:
            for long in b:
                long = long.rstrip("\r\n")
                if (long.count(short) > 0 and long != short and len(long) > 1):
                    updateShort(short,long)
                    updateLong(short,long)
                    print (short,'is in',long)
```
and if you want to test words once you've built a database:

```python
# print some demo words

import random

def randomWord(wordlist):
    word = random.choice(list(open(wordlist))).rstrip("\r\n")
    print(db.get(q.word == word))

for i in range(10):
    randomWord(wordlist)
```
