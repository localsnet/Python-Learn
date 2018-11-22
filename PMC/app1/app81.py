# Bug task1 Please add another conditional block to the program so that the program returns the definition of names
# that start with a capital letter.
import json
# 85 introduction to get_close_matches
from difflib import get_close_matches

filename = 'data.json'
# PCC way
# with open(filename) as f_obj:
# data=json.load(f_obj)
# PMC way
data = json.load(open(filename))
# Check some key
# print(data["sky"])
word = input('Type word for definition: ')


def wordfind(w):
    '''Find definition by word'''
    # 83 Implementing Case Sensitivity
    w = w.lower()
    print (w)

    # check type of data
    print(type(data))
    print(type(data.keys()))
    #print(type(get_close_matches(w, data.keys())[0]))
    # Only for existed keys    print(type((data[w])))
    # First we expect correct word by checking it in dictionary keys, otherwise try to find it with get_close_matches in elif block
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]



    # 82 Accounting for non-existing Words. i.e. typos
    # The positive result is 3 according default ratio of get_close_matches
    elif len(get_close_matches(w, data.keys())) > 0:

        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])

        if yn == "Y":
            # get_close_matches returns a list data with 3 items but an index 0 return a one word (string) of all  (is most close to desired word) and it was passed
            # passed as a dict key (argument) to the data dictionary which in turn will return its  value (list data type,
            # because a values stored in this way in current json file)   eventually.
            return data[get_close_matches(w, data.keys())[0]]

        elif yn == "N":

            return "The word doesn't exist. Please double check it."

        else:

            return "We didn't understand your entry."
    # Counting for Non-existing Words
    else:

        return "The word doesn't exist. Please double check it."


output = wordfind(word)
# check data type
print(type(output))
if type(output) == list:
    # Formatting the user's output in readable view (list to string)
    for item in output:
        print(item)
# So if was "N" it's a string and else block is the case
else:
    print(output)