#Write a separate program that reads in this value and prints the message
import json
filename='favnumber.json'
with open(filename) as f_obj:
    fav_number=json.load(f_obj)
print("I know your favorite number! It’s "+ fav_number)