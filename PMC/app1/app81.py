import json
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
# 83 Implementing Case Sensitivity
    w = w.lower()
#82 Accounting for non-existing Words
    if w in data:
        print(data[w])
    else:
        print('The word not found, check spelling')

wordfind(word)
