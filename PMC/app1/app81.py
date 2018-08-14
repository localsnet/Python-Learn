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

def wordfind():
    '''Find definition by word'''
    print(data[word])

wordfind()