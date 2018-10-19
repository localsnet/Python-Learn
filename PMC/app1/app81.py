import json
#85 introduction to get_close_matches
from difflib import get_close_matches
filename='data.json'
#PCC way
#with open(filename) as f_obj:
# data=json.load(f_obj)
#PMC way
data = json.load(open(filename))
#Check some key
#print(data["sky"])
word = input('Type word for definition: ')

def wordfind(w):
    '''Find definition by word'''
#83 Implementing Case Sensitivity
    w = w.lower()
#82 Accounting for non-existing Words
    # check type of data
    print(type(data))
    print(type(data.keys()))
    print(type((data[w])))

    if w in data:
        print(data[w])

    else:
        print(get_close_matches(w, data.keys()))# > 0:





wordfind(word)
