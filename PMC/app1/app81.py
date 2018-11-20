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
#The positive result is 3 according default ratio of get_close_matches
    print(len(get_close_matches(w, data.keys())))
#Only for existed keys    print(type((data[w])))

    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:

        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])

        if yn == "Y":

            return data[get_close_matches(w, data.keys())[0]]

        elif yn == "N":

            return "The word doesn't exist. Please double check it."

        else:

            return "We didn't understand your entry."

    else:

        return "The word doesn't exist. Please double check it."




output = wordfind(word)
print(type(output))
if type(output) == list:
# So if was "N" it's a string and else block is the case
    for item in output:
        print(item)
else:
    print(output)